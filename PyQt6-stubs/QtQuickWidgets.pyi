# The PEP 484 type hints stub file for the QtQuickWidgets module.
#
# Generated by SIP 6.0.2
#
# Copyright (c) 2021 Riverbank Computing Limited <info@riverbankcomputing.com>
#
# This file is part of PyQt6.
#
# This file may be used under the terms of the GNU General Public License
# version 3.0 as published by the Free Software Foundation and appearing in
# the file LICENSE included in the packaging of this file.  Please review the
# following information to ensure the GNU General Public License version 3.0
# requirements will be met: http://www.gnu.org/copyleft/gpl.html.
#
# If you do not wish to use this file under the terms of the GPL version 3.0
# then you may purchase a commercial license.  For more information contact
# info@riverbankcomputing.com.
#
# This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
# WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

# Support for QDate, QDateTime and QTime.
import datetime
import enum
import typing

import PyQt6.sip
from PyQt6 import QtCore, QtGui, QtQml, QtQuick, QtWidgets

# Convenient type aliases.
PYQT_SIGNAL = typing.Union[QtCore.pyqtSignal, QtCore.pyqtBoundSignal]
PYQT_SLOT = typing.Union[typing.Callable[..., None], QtCore.pyqtBoundSignal]

class QQuickWidget(QtWidgets.QWidget):
    class Status(enum.Enum):
        Null = ...  # type: QQuickWidget.Status
        Ready = ...  # type: QQuickWidget.Status
        Loading = ...  # type: QQuickWidget.Status
        Error = ...  # type: QQuickWidget.Status
    class ResizeMode(enum.Enum):
        SizeViewToRootObject = ...  # type: QQuickWidget.ResizeMode
        SizeRootObjectToView = ...  # type: QQuickWidget.ResizeMode
    @typing.overload
    def __init__(
        self, parent: typing.Optional[QtWidgets.QWidget] = ...
    ) -> None: ...
    @typing.overload
    def __init__(
        self, engine: QtQml.QQmlEngine, parent: QtWidgets.QWidget
    ) -> None: ...
    @typing.overload
    def __init__(
        self,
        source: QtCore.QUrl,
        parent: typing.Optional[QtWidgets.QWidget] = ...,
    ) -> None: ...
    def focusNextPrevChild(self, next: bool) -> bool: ...
    def quickWindow(self) -> QtQuick.QQuickWindow: ...
    def setClearColor(
        self, color: typing.Union[QtGui.QColor, QtCore.Qt.GlobalColor]
    ) -> None: ...
    def grabFramebuffer(self) -> QtGui.QImage: ...
    def paintEvent(self, event: QtGui.QPaintEvent) -> None: ...
    def dropEvent(self, a0: QtGui.QDropEvent) -> None: ...
    def dragLeaveEvent(self, a0: QtGui.QDragLeaveEvent) -> None: ...
    def dragMoveEvent(self, a0: QtGui.QDragMoveEvent) -> None: ...
    def dragEnterEvent(self, a0: QtGui.QDragEnterEvent) -> None: ...
    def focusOutEvent(self, event: QtGui.QFocusEvent) -> None: ...
    def focusInEvent(self, event: QtGui.QFocusEvent) -> None: ...
    def event(self, a0: QtCore.QEvent) -> bool: ...
    def wheelEvent(self, a0: QtGui.QWheelEvent) -> None: ...
    def hideEvent(self, a0: QtGui.QHideEvent) -> None: ...
    def showEvent(self, a0: QtGui.QShowEvent) -> None: ...
    def mouseDoubleClickEvent(self, a0: QtGui.QMouseEvent) -> None: ...
    def mouseMoveEvent(self, a0: QtGui.QMouseEvent) -> None: ...
    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent) -> None: ...
    def mousePressEvent(self, a0: QtGui.QMouseEvent) -> None: ...
    def keyReleaseEvent(self, a0: QtGui.QKeyEvent) -> None: ...
    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None: ...
    def timerEvent(self, a0: QtCore.QTimerEvent) -> None: ...
    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None: ...
    sceneGraphError: typing.ClassVar[QtCore.pyqtSignal]
    statusChanged: typing.ClassVar[QtCore.pyqtSignal]
    def setSource(self, a0: QtCore.QUrl) -> None: ...
    def format(self) -> QtGui.QSurfaceFormat: ...
    def setFormat(self, format: QtGui.QSurfaceFormat) -> None: ...
    def initialSize(self) -> QtCore.QSize: ...
    def sizeHint(self) -> QtCore.QSize: ...
    def errors(self) -> typing.List[QtQml.QQmlError]: ...
    def status(self) -> "QQuickWidget.Status": ...
    def setResizeMode(self, a0: "QQuickWidget.ResizeMode") -> None: ...
    def resizeMode(self) -> "QQuickWidget.ResizeMode": ...
    def rootObject(self) -> QtQuick.QQuickItem: ...
    def rootContext(self) -> QtQml.QQmlContext: ...
    def engine(self) -> QtQml.QQmlEngine: ...
    def source(self) -> QtCore.QUrl: ...
