#include "stopwatch.h"
#include <QString>
#include <QtGui>
#include <QWidget>
#include <QTime>

stopwatch::stopwatch(QWidget *parent)
    : QWidget(parent)

{
	num = new QLCDNumber(this);
	num->setDigitCount(10);

	time = new QTime();
	timer = new QTimer(this);
	connect(timer, SIGNAL(timeout()), this, SLOT(showTime()));

	layout = new QVBoxLayout;
	hlayout = new QHBoxLayout;
	start = new QPushButton("Start");
	stop = new QPushButton("Stop");
	start->setMinimumHeight(80);
	stop->setMinimumHeight(80);

	connect(start,SIGNAL(clicked()),this,SLOT(startTime()));
	connect(stop,SIGNAL(clicked()),this,SLOT(stopTime()));
	QString text = "00:00:00.0";
	num->display(text);
	num->setSegmentStyle(QLCDNumber::Filled);

	hlayout->addWidget(start);
	hlayout->addWidget(stop);
	layout->addWidget(num);
	layout->addLayout(hlayout);
	setLayout(layout);
	resize(320,240);
}
 
stopwatch::~stopwatch()
{
    // No need to delete any object that has a parent which is properly deleted.
 
}


void stopwatch::startTime()
{
	start->setDisabled(1);
	stop->setEnabled(1);
	timer->start(100);
	time->start();
}
 
void stopwatch::stopTime()
{
	stop->setDisabled(1);
	start->setEnabled(1);
	timer->stop();
}
 
 
void stopwatch::showTime()
{
	int ms = time->elapsed();
	int tenth = (ms % 1000) / 100;
	int sec = (ms / 1000) % 60;
	int min = (ms / 1000 / 60) % 60;
	int hr = (ms / 1000 / 60 / 60);
	
	QString text =QString("%1:%2:%3.%4")
	.arg(hr, 2, 10, QLatin1Char('0'))
	.arg(min, 2, 10, QLatin1Char('0'))
	.arg(sec, 2, 10, QLatin1Char('0'))
	.arg(tenth, 1, 10, QLatin1Char('0'));
	num->display(text);
}
