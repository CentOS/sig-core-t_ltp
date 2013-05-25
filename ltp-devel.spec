#
# RPM Package Manager (RPM) spec file for ltp-devel
#
Summary: Linux Test Project (LTP) Software Development Kit (SDK)
Name: ltp-devel
Version: 2.0
Release: 0.0
Prefix: /opt/ltp
License: GPL
Group: Development/Libraries
URL: http://www.linuxtestproject.org
Vendor: IBM Corp
Packager: Subrata Modak <subrata.modak@@in.ibm.com>
AutoReqProv:    0
Provides:       LTP
#ExclusiveArch:  i386
ExclusiveOS:    linux
%description
This is a development package of the Linux Test Project (LTP).
It is intended to be used to build testcases using the provided API.
%files
/opt/ltp/lib/libltp.a
${prefix}/share/pkgconfig/ltp.pc
/opt/ltp/bin/ltp-pan
/opt/ltp/bin/ltp-scanner
/opt/ltp/bin/ltp-bump
/opt/ltp/include/linux_syscall_numbers.h
/opt/ltp/include/libtestsuite.h
/opt/ltp/include/usctest.h
/opt/ltp/include/string_to_tokens.h
/opt/ltp/include/bytes_by_prefix.h
/opt/ltp/include/databin.h
/opt/ltp/include/open_flags.h
/opt/ltp/include/write_log.h
/opt/ltp/include/dataascii.h
/opt/ltp/include/forker.h
/opt/ltp/include/compiler.h
/opt/ltp/include/test.h
/opt/ltp/include/tlibio.h
/opt/ltp/include/pattern.h
/opt/ltp/include/file_lock.h
/opt/ltp/include/random_range.h
/opt/ltp/include/search_path.h
/opt/ltp/include/rmobj.h
${datarootdir}/man/man3/tst_tmpdir.3
${datarootdir}/man/man3/random_range_seed.3
${datarootdir}/man/man3/pattern.3
${datarootdir}/man/man3/parse_ranges.3
${datarootdir}/man/man3/usctest.3
${datarootdir}/man/man3/random_range.3
${datarootdir}/man/man3/forker.3
${datarootdir}/man/man3/rmobj.3
${datarootdir}/man/man3/parse_open_flags.3
${datarootdir}/man/man3/tst_res.3
${datarootdir}/man/man3/write_log.3
${datarootdir}/man/man3/bytes_by_prefix.3
${datarootdir}/man/man3/tst_set_error.3
${datarootdir}/man/man3/parse_opts.3
${datarootdir}/man/man3/string_to_tokens.3
${datarootdir}/man/man3/tst_sig.3
${datarootdir}/man/man3/get_attrib.3
${datarootdir}/man/man1/ltp-pan.1
${datarootdir}/man/man1/doio.1
${datarootdir}/man/man1/iogen.1
${datarootdir}/man/man1/ltp-bump.1
# Post-install stuff would go here.
#EOF

