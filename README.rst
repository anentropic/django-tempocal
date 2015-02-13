===============
django-tempocal
===============

An extension of the Python stdlib's ``calendar.HTMLCalendar`` that makes use of Django templates to customise the output. After all, it's pretty lame having hard-coded HTML output.

Usage:

``pip install django-tempocal``

Add ``'tempocal'`` to your ``INSTALLED_APPS``.

.. code:: python

    from tempocal import TemplatedCalendar

    def myview(request, year, month):
        calendar = TemplatedCalendar()
        month_table = calendar.formatmonth(int(year), int(month))
        return render_to_response('myview.html', {'month_table': month_table})

This will use the ``tempocal/month.html`` that comes with tempocal, you can override this via the normal Django mechanism.
