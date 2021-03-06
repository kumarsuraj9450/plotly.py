from plotly.basedatatypes import BaseTraceHierarchyType
import copy


class Dimension(BaseTraceHierarchyType):

    # label
    # -----
    @property
    def label(self):
        """
        Sets the label corresponding to this splom dimension.
    
        The 'label' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        return self['label']

    @label.setter
    def label(self, val):
        self['label'] = val

    # values
    # ------
    @property
    def values(self):
        """
        Sets the dimension values to be plotted.
    
        The 'values' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        return self['values']

    @values.setter
    def values(self, val):
        self['values'] = val

    # valuessrc
    # ---------
    @property
    def valuessrc(self):
        """
        Sets the source reference on plot.ly for  values .
    
        The 'valuessrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        return self['valuessrc']

    @valuessrc.setter
    def valuessrc(self, val):
        self['valuessrc'] = val

    # visible
    # -------
    @property
    def visible(self):
        """
        Determines whether or not this dimension is shown on the graph.
        Note that even visible false dimension contribute to the
        default grid generate by this splom trace.
    
        The 'visible' property must be specified as a bool
        (either True, or False)

        Returns
        -------
        bool
        """
        return self['visible']

    @visible.setter
    def visible(self, val):
        self['visible'] = val

    # property parent name
    # --------------------
    @property
    def _parent_path_str(self):
        return 'splom'

    # Self properties description
    # ---------------------------
    @property
    def _prop_descriptions(self):
        return """\
        label
            Sets the label corresponding to this splom dimension.
        values
            Sets the dimension values to be plotted.
        valuessrc
            Sets the source reference on plot.ly for  values .
        visible
            Determines whether or not this dimension is shown on
            the graph. Note that even visible false dimension
            contribute to the default grid generate by this splom
            trace.
        """

    def __init__(
        self,
        arg=None,
        label=None,
        values=None,
        valuessrc=None,
        visible=None,
        **kwargs
    ):
        """
        Construct a new Dimension object
        
        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of plotly.graph_objs.splom.Dimension
        label
            Sets the label corresponding to this splom dimension.
        values
            Sets the dimension values to be plotted.
        valuessrc
            Sets the source reference on plot.ly for  values .
        visible
            Determines whether or not this dimension is shown on
            the graph. Note that even visible false dimension
            contribute to the default grid generate by this splom
            trace.

        Returns
        -------
        Dimension
        """
        super(Dimension, self).__init__('dimensions')

        # Validate arg
        # ------------
        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = copy.copy(arg)
        else:
            raise ValueError(
                """\
The first argument to the plotly.graph_objs.splom.Dimension 
constructor must be a dict or 
an instance of plotly.graph_objs.splom.Dimension"""
            )

        # Import validators
        # -----------------
        from plotly.validators.splom import (dimension as v_dimension)

        # Initialize validators
        # ---------------------
        self._validators['label'] = v_dimension.LabelValidator()
        self._validators['values'] = v_dimension.ValuesValidator()
        self._validators['valuessrc'] = v_dimension.ValuessrcValidator()
        self._validators['visible'] = v_dimension.VisibleValidator()

        # Populate data dict with properties
        # ----------------------------------
        _v = arg.pop('label', None)
        self.label = label if label is not None else _v
        _v = arg.pop('values', None)
        self.values = values if values is not None else _v
        _v = arg.pop('valuessrc', None)
        self.valuessrc = valuessrc if valuessrc is not None else _v
        _v = arg.pop('visible', None)
        self.visible = visible if visible is not None else _v

        # Process unknown kwargs
        # ----------------------
        self._process_kwargs(**dict(arg, **kwargs))
