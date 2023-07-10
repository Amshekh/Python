#include <Python.h>

extern long BoxVolume(long, long, long, short);

static PyObject* DimExc;

PyObject* GetBoxArea(PyObject* module, PyObject* args)
{
	PyObject* result = NULL;
	long l, b, h;

	if(PyArg_ParseTuple(args, "lll", &l, &b, &h))
	{
		long area = 2 * (l * b + b * h + l * h);
		result = Py_BuildValue("l", area);
	}

	return result;
}

PyObject* GetBoxVolume(PyObject* module, PyObject* args)
{
	PyObject* result = NULL;
	long l, b, h;
	short t;

	if(PyArg_ParseTuple(args, "lllh", &l, &b, &h, &t))
	{
		if(l < 2 * t || b < 2 * t || h < 2 * t)
			PyErr_SetString(DimExc, "Invalid box thickness.");
		else
		{
			long volume = BoxVolume(l, b, h, t);
			result = Py_BuildValue("l", volume);
		}
	}

	return result;
}

void initBox(void)
{
	static PyMethodDef methods[] = {
		{"OuterArea", GetBoxArea, METH_VARARGS},
		{"InnerVolume", GetBoxVolume, METH_VARARGS},
		{NULL}
	};
	PyObject* module = Py_InitModule("Box", methods);

	DimExc = PyErr_NewException("Box.DimensionError", NULL, NULL);
	Py_INCREF(DimExc);
	PyModule_AddObject(module, "DimensionError", DimExc);
}















