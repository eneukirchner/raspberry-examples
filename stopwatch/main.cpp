#include <QApplication>
#include "stopwatch.h"

 int main(int argc, char *argv[])
 {
     QApplication app(argc, argv);
     stopwatch watch;
     watch.show();
     return app.exec();
 }
