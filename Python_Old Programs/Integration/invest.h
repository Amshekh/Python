#ifndef INVEST_H
#define INVEST_H

typedef struct{
	long id;
	double amount;
	long period;
}FixedDeposit;

typedef float (*Scheme)(double, long);

int InitFixedDeposit(double, long, FixedDeposit*);

double GetMaturityValue(FixedDeposit*, Scheme);

#endif











