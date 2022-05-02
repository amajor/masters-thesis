import attr

@attr.s
class CommitLog(object):
    author=attr.ib()
    date=attr.ib()
    message=attr.ib()
    lines_added=attr.ib()
    lines_removed=attr.ib()
    module = attr.ib(default=None)


    @property
    def is_bug(self):
        if 'bug' in self.message or \
            'fix' in self.message or \
            'typo'in self.message:
            return True

        return False


@attr.s
class PylintMetrics(object):
    global_note = attr.ib(default='-')
    convention = attr.ib(default='-')
    refactor = attr.ib(default= '-')
    code_lines = attr.ib(default= '-')
    classes = attr.ib(default='-')

@attr.s
class ModuleMetrics(object):
    module_name =attr.ib(default='')
    pylint_metrics = attr.ib(default=attr.Factory(list))
    git_metrics = attr.ib(default=attr.Factory(list))

    def total_commits(self):
        return len(self.git_metrics)

    def total_fixes(self):
        count = 0
        for log in self.git_metrics:
            if log.is_bug():
                count += 1

        return count




