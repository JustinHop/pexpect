#!/usr/bin/env python
import pexpect
import unittest
import commands
import sys

class ExpectTestCase(unittest.TestCase):
    #def runTest (self):
        
    def test_run_out (self):
        """This assumes that the tested platform has less than 1000 pty devices.
	"""
	plist=[]
        for count in range (0,1000):
		try:
			plist.append (pexpect.spawn('/bin/ls -l'))
		except pexpect.ExceptionPexpect, e:
			return
		else:
			self.fail ('Expected ExceptionPexpect.')
	self.fail ('Could not run out of pty devices. This may be OK.')

if __name__ == '__main__':
    unittest.main()

suite = unittest.makeSuite(ExpectTestCase,'test')

#fout = open('delete_me_1','wb')
#fout.write(the_old_way)
#fout.close
#fout = open('delete_me_2', 'wb')
#fout.write(the_new_way)
#fout.close
