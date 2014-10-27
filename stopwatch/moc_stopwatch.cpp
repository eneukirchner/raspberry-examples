/****************************************************************************
** Meta object code from reading C++ file 'stopwatch.h'
**
** Created: Fri Oct 24 18:45:19 2014
**      by: The Qt Meta Object Compiler version 63 (Qt 4.8.2)
**
** WARNING! All changes made in this file will be lost!
*****************************************************************************/

#include "stopwatch.h"
#if !defined(Q_MOC_OUTPUT_REVISION)
#error "The header file 'stopwatch.h' doesn't include <QObject>."
#elif Q_MOC_OUTPUT_REVISION != 63
#error "This file was generated using the moc from 4.8.2. It"
#error "cannot be used with the include files from this version of Qt."
#error "(The moc has changed too much.)"
#endif

QT_BEGIN_MOC_NAMESPACE
static const uint qt_meta_data_stopwatch[] = {

 // content:
       6,       // revision
       0,       // classname
       0,    0, // classinfo
       3,   14, // methods
       0,    0, // properties
       0,    0, // enums/sets
       0,    0, // constructors
       0,       // flags
       0,       // signalCount

 // slots: signature, parameters, type, tag, flags
      10,   21,   21,   21, 0x08,
      22,   21,   21,   21, 0x08,
      34,   21,   21,   21, 0x08,

       0        // eod
};

static const char qt_meta_stringdata_stopwatch[] = {
    "stopwatch\0stopTime()\0\0startTime()\0"
    "showTime()\0"
};

void stopwatch::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    if (_c == QMetaObject::InvokeMetaMethod) {
        Q_ASSERT(staticMetaObject.cast(_o));
        stopwatch *_t = static_cast<stopwatch *>(_o);
        switch (_id) {
        case 0: _t->stopTime(); break;
        case 1: _t->startTime(); break;
        case 2: _t->showTime(); break;
        default: ;
        }
    }
    Q_UNUSED(_a);
}

const QMetaObjectExtraData stopwatch::staticMetaObjectExtraData = {
    0,  qt_static_metacall 
};

const QMetaObject stopwatch::staticMetaObject = {
    { &QWidget::staticMetaObject, qt_meta_stringdata_stopwatch,
      qt_meta_data_stopwatch, &staticMetaObjectExtraData }
};

#ifdef Q_NO_DATA_RELOCATION
const QMetaObject &stopwatch::getStaticMetaObject() { return staticMetaObject; }
#endif //Q_NO_DATA_RELOCATION

const QMetaObject *stopwatch::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->metaObject : &staticMetaObject;
}

void *stopwatch::qt_metacast(const char *_clname)
{
    if (!_clname) return 0;
    if (!strcmp(_clname, qt_meta_stringdata_stopwatch))
        return static_cast<void*>(const_cast< stopwatch*>(this));
    return QWidget::qt_metacast(_clname);
}

int stopwatch::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QWidget::qt_metacall(_c, _id, _a);
    if (_id < 0)
        return _id;
    if (_c == QMetaObject::InvokeMetaMethod) {
        if (_id < 3)
            qt_static_metacall(this, _c, _id, _a);
        _id -= 3;
    }
    return _id;
}
QT_END_MOC_NAMESPACE
