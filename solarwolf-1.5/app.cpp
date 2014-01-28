//  This simple program is compile-linked to the Python interpreter,
//  so it can provide a "binary" image for the Python program it really
//  runs, and all kinds of BeOS loading semantics can be attached here -
//  mime types, icons, single-launch, bla bla.  This example is the most
//  minimal, crude but reasonably effective.
//
//  It's also possible to implement BApplication in C++ here, then import
//  the main Python module (now rewritten of course to omit its BApplication
//  class wrapper) and call its exported  methods.  I don't see anything
//  to be gained from this, but there's a lot I don't know.  Anyway, to do
//  it you need to add a tweak to BApplication.cpp, to set "be_app" from
//  the FromBApplication() function.

//#include <sys/file.h>
//#include <stdio.h>
//#include <unistd.h>

//Weeeee lack of realpath and dirname rocks
#include <Entry.h>
#include <Path.h>

#ifndef PYTHON_INSTALL_PREFIX
#define PYTHON_INSTALL_PREFIX "/boot/home/config"
#endif

#include <Python.h>

static void
setup_interpreter(int argc, char **argv, const char *appdir)
{
	char path[256];
	static const char prefix[] = PYTHON_INSTALL_PREFIX;
	char python[12];

	Py_SetProgramName(argv[0]);
	Py_Initialize();
	PySys_SetArgv(argc, argv);

	sprintf(python, "python%d.%d", PY_MAJOR_VERSION, PY_MINOR_VERSION);
	sprintf(path, "%s:%s/lib/%s:%s/lib/%s/plat-beos5:%s/lib/%s/lib-dynload",
		appdir,
		prefix, python,
		prefix, python,
		prefix, python);
		sprintf(path, "%s:%s/lib/%s/site-packages", path, prefix, python);
	PySys_SetPath(path);
}

int
main(int argc, char **argv)
{
	FILE *py;
	char *nm;
	static char progfile[] = PYTHONMAIN;
	static char defdir[] = ".";
	const char *ppath;
	char pname[B_FILE_NAME_LENGTH];
	char *progbase, *progdir;

	BPath path;
	BEntry entry(argv[0], false);
	entry.GetParent(&entry);
	entry.GetPath(&path);
	ppath = path.Path();
	entry.GetName(pname);

	chdir(ppath);
	py = fopen(progfile, "r");
	if (!py) {
		perror(progfile);
		exit(2);
	}

	setup_interpreter(argc, argv, ppath);

	PyRun_AnyFile(py, pname);
	if (PyErr_Occurred()) {
		PyErr_Print();
		exit(1);
	} else
		exit(0);
}
