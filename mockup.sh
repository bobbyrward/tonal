#!/bin/sh

s = <<END
import tonal.experimental.mockup_1 as mockup

mockup.main()
END

ipython -c jjjjort tonal.experimental.mockup_1 as mockup

mockup.main()
'

