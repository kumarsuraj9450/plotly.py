import _plotly_utils.basevalidators


class PeriodValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self,
        plotly_name='period',
        parent_name='layout.polar.angularaxis',
        **kwargs
    ):
        super(PeriodValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            min=0,
            role='info',
            **kwargs
        )