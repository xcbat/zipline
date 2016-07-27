from warnings import catch_warnings, WarningMessage


class WarningsCatcher(catch_warnings):
    """
    Subclass of warnings.catch_warnings that takes a list of warning types to
    ignore.
    """
    def __init__(self, types_to_ignore=None):
        super(WarningsCatcher, self).__init__()

        self._types_to_ignore = set(types_to_ignore or [])

    def __enter__(self):
        super(WarningsCatcher, self).__enter__()

        log = []

        def show_warning(*args, **kwargs):
            if args[1] in self._types_to_ignore:
                return

            log.append(WarningMessage(*args, **kwargs))

        self._module.showwarning = show_warning
        return log
