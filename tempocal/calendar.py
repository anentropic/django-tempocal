import sys
from calendar import HTMLCalendar, day_abbr, month_name, January

from django.template.loader import render_to_string


class TemplatedCalendar(HTMLCalendar):
    """
    The same as HTMLCalendar but we override all the output methods with
    templated versions.

    To use, add `tempocal` to your Django INSTALLED_APPS. Of course, you can
    override these templates like with any Django app.
    """

    templates = {
        'day': 'tempocal/day.html',
        'week': 'tempocal/week.html',
        'weekday': 'tempocal/weekday.html',
        'weekheader': 'tempocal/weekheader.html',
        'monthname': 'tempocal/monthname.html',
        'month': 'tempocal/month.html',
        'year': 'tempocal/year.html',
        'yearpage': 'tempocal/yearpage.html',
        'emptymonth': 'tempocal/emptymonth.html',
    }

    def formatday(self, day, weekday):
        """
        Return a day as a table cell.
        """
        if day == 0:
            css_class = 'noday'
        else:
            css_class = self.cssclasses[weekday]

        return render_to_string(
            self.templates['day'],
            {
                'css_class': css_class,
                'day': day,
            })

    def formatweek(self, theweek):
        """
        Return a complete week as a table row.
        """
        return render_to_string(
            self.templates['week'],
            {
                'days': [self.formatday(d, wd) for (d, wd) in theweek],
            })

    def formatweekday(self, day):
        """
        Return a weekday name as a table header.
        """
        return render_to_string(
            self.templates['weekday'],
            {
                'css_class': self.cssclasses[day],
                'day': day_abbr[day],
            })

    def formatweekheader(self):
        """
        Return a header for a week as a table row.
        """
        return render_to_string(
            self.templates['weekheader'],
            {
                'days': [self.formatweekday(i) for i in self.iterweekdays()],
            })

    def formatmonthname(self, theyear, themonth, withyear=True):
        """
        Return a month name as a table row.
        """
        if withyear:
            s = '%s %s' % (month_name[themonth], theyear)
        else:
            s = '%s' % month_name[themonth]

        return render_to_string(
            self.templates['monthname'],
            {
                'month_name': s,
            })

    def formatmonth(self, theyear, themonth, withyear=True):
        """
        Return a formatted month as a table.
        """
        return render_to_string(
            self.templates['month'],
            {
                'month_name_row': self.formatmonthname(
                    theyear, themonth, withyear=withyear
                ),
                'week_header_row': self.formatweekheader(),
                'week_rows': [
                    self.formatweek(week)
                    for week in self.monthdays2calendar(theyear, themonth)
                ]
            }
        )

    def formatyear(self, theyear, width=3):
        """
        Return a formatted year as a table of tables.
        """
        rows = []
        for i in xrange(January, January + 12, width):
            row = []
            for m in xrange(i, 13):
                if m > i + width:
                    # this is new logic compared to HTMLCalendar, which would
                    # just not output any TD cells after the end of months in
                    # range. if you want that behaviour then have an empty
                    # template, or delete the template item from
                    # self.templates. Otherwise you can render emptymonth.html
                    if 'emptymonth' in self.templates:
                        row.append(
                            render_to_string(self.templates['emptymonth'])
                        )
                    else:
                        row.append(None)
                else:
                    row.append(self.formatmonth(theyear, m, withyear=False))
            rows.append(row)

        return render_to_string(
            self.templates['year'],
            {
                'colspan': max(width, 1),
                'year': theyear,
                'rows': rows,
            })

    def formatyearpage(self, theyear, width=3, css='calendar.css',
                       encoding=None):
        """
        Return a formatted year as a complete HTML page.
        """
        if encoding is None:
            encoding = sys.getdefaultencoding()

        return render_to_string(
            self.templates['yearpage'],
            {
                'encoding': encoding,
                'css': css,
                'theyear': theyear,
                'year': self.formatyear(theyear, width),
            })
