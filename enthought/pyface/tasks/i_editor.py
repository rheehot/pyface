# Enthought library imports.
from enthought.traits.api import Any, Bool, Event, HasTraits, Interface, \
    Instance, Unicode, Vetoable, VetoableEvent


class IEditor(Interface):
    """ The base interface for all panes (central and dock) in a Task.
    """

    # The editor's user-visible name.
    name = Unicode

    # The toolkit-specific control that represents the editor.
    control = Any

    # The object that the editor is editing.
    obj = Any

    # Has the editor's object been modified but not saved?
    dirty = Bool

    # The editor area to which the editor belongs.
    editor_area = Instance(
        'enthought.pyface.tasks.i_editor_area_pane.IEditorAreaPane')

    # Fired when the editor has been requested to close.
    closing = VetoableEvent

    # Fired when the editor has been closed.
    closed = Event

    ###########################################################################
    # 'IEditor' interface.
    ###########################################################################

    def close(self):
        """ Close the editor.
        """

    def create(self, parent):
        """ Create and set the toolkit-specific control that represents the
            editor.
        """

    def destroy(self):
        """ Destroy the toolkit-specific control that represents the editor.
        """


class MEditor(HasTraits):
    """ Mixin containing common code for toolkit-specific implementations.
    """

    #### 'IEditor' interface ##################################################

    name = Unicode
    control = Any
    obj = Any
    dirty = Bool(False)
    editor_area = Instance(
        'enthought.pyface.tasks.i_editor_area_pane.IEditorAreaPane')

    closing = VetoableEvent
    closed = Event

    ###########################################################################
    # 'IEditor' interface.
    ###########################################################################

    def close(self):
        """ Close the editor.
        """
        if self.control is not None:
            self.closing = event = Vetoable()
            if not event.veto:
                self.editor_area.remove_editor(self)
                self.closed = True
