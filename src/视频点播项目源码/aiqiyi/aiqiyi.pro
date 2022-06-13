#-------------------------------------------------
#
# Project created by QtCreator 2021-06-15T10:06:08
#
#-------------------------------------------------
QT       += core gui
QT       +=  multimedia multimediawidgets
QT       += multimedia
greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = aiqiyi
TEMPLATE = app

# The following define makes your compiler emit warnings if you use
# any feature of Qt which as been marked as deprecated (the exact warnings
# depend on your compiler). Please consult the documentation of the
# deprecated API in order to know how to port your code away from it.
DEFINES += QT_DEPRECATED_WARNINGS

# You can also make your code fail to compile if you use deprecated APIs.
# In order to do so, uncomment the following line.
# You can also select to disable deprecated APIs only up to a certain version of Qt.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0


SOURCES += main.cpp\
        widget.cpp \
    form.cpp \
    dongtu.cpp \
    user.cpp \
    data.cpp \
    skip.cpp \
    video.cpp \
    vidiowins.cpp \
    playwin.cpp

HEADERS  += widget.h \
    form.h \
    dongtu.h \
    user.h \
    data.h \
    skip.h \
    video.h \
    vidiowins.h \
    playwin.h

FORMS    += widget.ui \
    form.ui \
    dongtu.ui \
    video.ui \
    vidiowins.ui \
    videoplay.ui

RESOURCES += \
    ../build-aiqiyi-Desktop_Qt_5_8_0_MinGW_32bit-Debug/image.qrc

DISTFILES +=
