#include <Python.h>
#include <fcntl.h>
#include <sys/mman.h>

PyObject* GetSharedText(PyObject* module, PyObject* args)
{
	PyObject* result;
	int fdsm;

	fdsm = shm_open("testshm", O_RDONLY, 0);
	if(fdsm == -1) 
		result = Py_None;
	else
	{
		char* text = mmap(NULL, 4096, PROT_READ, 
			MAP_FILE | MAP_SHARED, fdsm, 0);
		result = Py_BuildValue("s", text);
		munmap(text, 4096);
		close(fdsm);
	}

	return result;
}

void initShMem(void)
{
	static PyMethodDef methods[] = {
		{"GetString", GetSharedText, METH_NOARGS},
		{NULL}
	};
	PyObject* module = Py_InitModule("ShMem", methods);
}
























