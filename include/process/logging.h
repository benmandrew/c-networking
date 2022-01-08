
#ifndef LOGGING_H
#define LOGGING_H

#include <stdarg.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void set_logfile_name(char *name);

int log_f(const char *format, ...);

#endif
