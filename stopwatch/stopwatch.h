
#ifndef STOPWATCH_H
#define STOPWATCH_H
 
#include <QtGui>
#include <QVBoxLayout>
#include <QPushButton>
#include <QLCDNumber>
#include <QTime>
#include <QTimer>
#include <QHBoxLayout>

class stopwatch : public QWidget
{
    Q_OBJECT
 
public:
	stopwatch(QWidget *parent = 0);
    ~stopwatch();
private slots:
    void stopTime();
    void startTime();
    void showTime();
private:
	QTime *time;
	QTimer *timer;
 
	QVBoxLayout *layout;
	QHBoxLayout *hlayout;
	QPushButton *start;
	QPushButton *stop;
    QLCDNumber *num;
};
 
#endif // STOPWATCH_H
