class PHPDirectoryNotFound(Exception):
    pass


class InvalidFileExtension(Exception):
    pass


class NoInterpreterFound(Exception):
    pass


class InvalidDocsDir(Exception):
    pass


content_types: dict = {'': 'application/pgp-encrypted', '.obd': 'application/x-msbinder',
                       '.dfac': 'application/vnd.dreamfactory',
                       '.cryptonote': 'application/vnd.rig.cryptonote', '.pml': 'application/vnd.ctc-posml',
                       '.f4v': 'video/x-f4v', '.rl':
                           'application/resource-lists+xml', '.ras': 'image/x-cmu-raster',
                       '.rar': 'application/x-rar-compressed', '.mrc':
                           'application/marc', '.bcpio': 'application/x-bcpio',
                       '.sdkm': 'application/vnd.solent.sdkm+xml', '.ecelp7470':
                           'audio/vnd.nuera.ecelp7470', '.bz': 'application/x-bzip', '.ait': 'application/vnd.dvb.ait',
                       '.bmp': 'image/bmp',
                       '.geo': 'application/vnd.dynageo',
                       '.air': 'application/vnd.adobe.air-application-installer-package+zip', '.bmi':
                           'application/vnd.bmi', '.tcl': 'application/x-tcl', '.dvi': 'application/x-dvi', '.gex':
                           'application/vnd.geometry-explorer', '.grxml': 'application/srgs+xml',
                       '.hpid': 'application/vnd.hp-hpid', '.ott':
                           'application/vnd.oasis.opendocument.text-template', '.otp':
                           'application/vnd.oasis.opendocument.presentation-template', '.ots':
                           'application/vnd.oasis.opendocument.spreadsheet-template', '.hlp': 'application/winhlp',
                       '.p10':
                           'application/pkcs10', '.csv': 'text/csv', '.nml': 'application/vnd.enliven',
                       '.csp': 'application/vnd.commonspace',
                       '.sus': 'application/vnd.sus-calendar', '.css': 'text/css', '.otg':
                           'application/vnd.oasis.opendocument.graphics-template', '.otf': 'application/x-font-otf',
                       '.csh':
                           'application/x-csh', '.bdf': 'application/x-font-bdf', '.pdb': 'application/vnd.palm',
                       '.sub':
                           'image/vnd.dvb.subtitle', '.es': 'application/ecmascript', '.uri': 'text/uri-list',
                       '.atomsvc':
                           'application/atomsvc+xml', '.xul': 'application/vnd.mozilla.xul+xml',
                       '.chm': 'application/vnd.ms-htmlhelp', '.xml':
                           'application/xml', '.umj': 'application/vnd.umajin', '.fig': 'application/x-xfig', '.cab':
                           'application/vnd.ms-cab-compressed', '.tsv': 'text/tab-separated-values',
                       '.ltf': 'application/vnd.frogans.ltf',
                       '.sis': 'application/vnd.symbian.install', '.prc': 'application/x-mobipocket-ebook', '.pre':
                           'application/vnd.lotus-freelance', '.prf': 'application/pics-rules',
                       '.car': 'application/vnd.curl.car', '.tsd':
                           'application/timestamped-data', '.dd2': 'application/vnd.oma.dd2+xml',
                       '.gsf': 'application/x-font-ghostscript',
                       '.tcap': 'application/vnd.3gpp2.tcap', '.ief': 'image/ief',
                       '.c4g': 'application/vnd.clonk.c4group', '.texinfo':
                           'application/x-texinfo', '.mp4a': 'audio/mp4', '.fpx': 'image/vnd.fpx',
                       '.viv': 'video/vnd.vivo', '.ddd':
                           'application/vnd.fujixerox.ddd', '.link66': 'application/vnd.route66.link66+xml', '.tmo':
                           'application/vnd.tmobile-livetv', '.ext': 'application/vnd.novadigm.ext',
                       '.exi': 'application/exi', '.csml':
                           'chemical/x-csml', '.mus': 'application/vnd.musician',
                       '.opf': 'application/oebps-package+xml', '.exe':
                           'application/x-msdownload', '.xpw': 'application/vnd.intercon.formnet',
                       '.xpr': 'application/vnd.is-xpr', '.xps':
                           'application/vnd.ms-xpsdocument', '.pbm': 'image/x-portable-bitmap',
                       '.dsc': 'text/prs.lines.tag', '.res':
                           'application/x-dtbresource+xml', '.rep': 'application/vnd.businessobjects',
                       '.adp': 'audio/adpcm', '.torrent':
                           'application/x-bittorrent', '.xpi': 'application/x-xpinstall', '.m21': 'application/mp21',
                       '.spq':
                           'application/scvp-vp-request', '.spp': 'application/scvp-vp-response', '.yaml': 'text/yaml',
                       '.ami':
                           'application/vnd.amiga.ami', '.fm': 'application/vnd.framemaker',
                       '.ram': 'audio/x-pn-realaudio', '.dssc':
                           'application/dssc+der', '.fh': 'image/x-freehand', '.pic': 'image/x-pict', '.spf':
                           'application/vnd.yamaha.smaf-phrase', '.spl': 'application/x-futuresplash',
                       '".atom': 'application/atom+xml',
                       '.mgp': 'application/vnd.osgeo.mapguide.package', '.emma': 'application/emma+xml',
                       '.eml': 'message/rfc822', 'N/A':
                           'application/andrew-inset', '.gac': 'application/vnd.groove-account',
                       '.cww': 'application/prs.cww', '.efif':
                           'application/vnd.picsel', '.yin': 'application/yin+xml', '.wad': 'application/x-doom',
                       '.saf':
                           'application/vnd.yamaha.smaf-audio', '.txf': 'application/vnd.mobius.txf',
                       '.utz': 'application/vnd.uiq.theme',
                       '.txd': 'application/vnd.genomatix.tuxedo', '.wav': 'audio/x-wav', '.rsd': 'application/rsd+xml',
                       '.xsm':
                           'application/vnd.syncml+xml', '.xbm': 'image/x-xbitmap', '.txt': 'text/plain', '.sse':
                           'application/vnd.kodak-descriptor', '.xbd': 'application/vnd.fujixerox.docuworks.binder',
                       '.wax': 'audio/x-ms-wax',
                       '.mlp': 'application/vnd.dolby.mlp', '.twd': 'application/vnd.simtech-mindmapper',
                       '.dna': 'application/vnd.dna',
                       '.ahead': 'application/vnd.ahead.space', '.fnc': 'application/vnd.frogans.fnc',
                       '.xif': 'image/vnd.xiff', '.dae':
                           'model/vnd.collada+xml', '.daf': 'application/vnd.mobius.daf',
                       '.cer': 'application/pkix-cert', '.smf':
                           'application/vnd.stardivision.math', '.ttf': 'application/x-font-ttf', '.dotm':
                           'application/vnd.ms-word.template.macroenabled.12', '.smi': 'application/smil+xml', '.p7r':
                           'application/x-pkcs7-certreqresp', '.gxt': 'application/vnd.geonext',
                       '.jisp': 'application/vnd.jisp', '.sfs':
                           'application/vnd.spotfire.sfs', '.imp': 'application/vnd.accpac.simply.imp',
                       '.ktx': 'image/ktx', '.ogv':
                           'video/ogg', '.movie': 'video/x-sgi-movie', '.dxp': 'application/vnd.spotfire.dxp', '.kia':
                           'application/vnd.kidspiration', '.tar': 'application/x-tar',
                       '.pnm': 'image/x-portable-anymap', '.mqy':
                           'application/vnd.mobius.mqy', '.dxf': 'image/vnd.dxf',
                       '.rnc': 'application/relax-ng-compact-syntax', '.tao':
                           'application/vnd.tao.intent-module-archive', '.xlsx':
                           'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                       '.wvx': 'video/x-ms-wvx', '.gdl':
                           'model/vnd.gdl', '.hpgl': 'application/vnd.hp-hpgl', '.dotx':
                           'application/vnd.openxmlformats-officedocument.wordprocessingml.template', '.ecelp9600':
                           'audio/vnd.nuera.ecelp9600', '.cu': 'application/cu-seeme',
                       '.chrt': 'application/vnd.kde.kchart', '.wsdl':
                           'application/wsdl+xml', '.dwg': 'image/vnd.dwg', '.dwf': 'model/vnd.dwf',
                       '.fg5': 'application/vnd.fujitsu.oasysgp',
                       '.aif': 'audio/x-aiff', '.ei6': 'application/vnd.pg.osasli',
                       '.svc': 'application/vnd.dvb.service', '.mcd':
                           'application/vnd.mcd', '".jpeg': 'image/jpeg', '.nnd': 'application/vnd.noblenet-directory',
                       '.pgn':
                           'application/x-chess-pgn', '.str': 'application/vnd.pg.format',
                       '.g2w': 'application/vnd.geoplan', '.stw':
                           'application/vnd.sun.xml.writer.template',
                       '.sti': 'application/vnd.sun.xml.impress.template', '.nns':
                           'application/vnd.noblenet-sealer', '.stk': 'application/hyperstudio',
                       '.crl': 'application/pkix-crl', '.ipfix':
                           'application/ipfix', '.stl': 'application/vnd.ms-pki.stl',
                       '.osf': 'application/vnd.yamaha.openscoreformat', '.bed':
                           'application/vnd.realvnc.bed', '.stc': 'application/vnd.sun.xml.calc.template',
                       '.crd': 'application/x-mscardfile',
                       '.std': 'application/vnd.sun.xml.draw.template', '.stf': 'application/vnd.wt.stf',
                       '.gmx': 'application/vnd.gmx',
                       '.avi': 'video/x-msvideo', '.qfx': 'application/vnd.intu.qfx',
                       '.mrcx': 'application/marcxml+xml', '.cla':
                           'application/vnd.claymore', '.pwn': 'application/vnd.3m.post-it-notes',
                       '.wml': 'text/vnd.wap.wml', '.lwp':
                           'application/vnd.lotus-wordpro', '.pskcxml': 'application/pskc+xml',
                       '.wma': 'audio/x-ms-wma', '.wmf':
                           'application/x-msmetafile', '.wmd': 'application/x-ms-wmd', '.mcurl': 'text/vnd.curl.mcurl',
                       '.wmz':
                           'application/x-ms-wmz', '.clp': 'application/x-msclip', '.wmx': 'video/x-ms-wmx',
                       '.hps': 'application/vnd.hp-hps',
                       '.mc1': 'application/vnd.medcalcdata', '.xpm': 'image/x-xpixmap', '.wmv': 'video/x-ms-wmv',
                       '.p12':
                           'application/x-pkcs12', '.kpr': 'application/vnd.kde.kpresenter',
                       '.g3w': 'application/vnd.geospace', '.oa2':
                           'application/vnd.fujitsu.oasys2', '.oa3': 'application/vnd.fujitsu.oasys3',
                       '.gtar': 'application/x-gtar', '.p7m':
                           'application/pkcs7-mime', '.deb': 'application/x-debian-package',
                       '.p7b': 'application/x-pkcs7-certificates',
                       '.mts': 'model/vnd.mts', '.der': 'application/x-x509-ca-cert',
                       '.p7s': 'application/pkcs7-signature', '.ecelp4800':
                           'audio/vnd.nuera.ecelp4800', '.fxp': 'application/vnd.adobe.fxp',
                       '.acc': 'application/vnd.americandynamics.acc',
                       '.otc': 'application/vnd.oasis.opendocument.chart-template', '.c11amz':
                           'application/vnd.cluetrust.cartomobile-config-pkg', '.ace': 'application/x-ace-compressed',
                       '"':
                           '"application/ccxml+xml', '.acu': 'application/vnd.acucobol',
                       '.wmlsc': 'application/vnd.wap.wmlscriptc', '.oas':
                           'application/vnd.fujitsu.oasys', '.c11amc': 'application/vnd.cluetrust.cartomobile-config',
                       '.tex':
                           'application/x-tex', '.wri': 'application/x-mswrite',
                       '.irp': 'application/vnd.irepository.package+xml', '.wrl':
                           'model/vrml', '.pdf': 'application/pdf', '.ssf': 'application/vnd.epson.ssf',
                       '.sitx': 'application/x-stuffitx',
                       '.hal': 'application/vnd.hal+xml', '.tei': 'application/tei+xml', '.rtx': 'text/richtext',
                       '.meta4':
                           'application/metalink4+xml', '.irm': 'application/vnd.ibm.rights-management', '.joda':
                           'application/vnd.joost.joda-archive', '.rpst': 'application/vnd.nokia.radio-preset',
                       '.fdf': 'application/vnd.fdf',
                       '.uvs': 'video/vnd.dece.sd', '.rpss': 'application/vnd.nokia.radio-presets',
                       '.etx': 'text/x-setext', '.mfm':
                           'application/vnd.mfmp', '.wbmp': 'image/vnd.wap.wbmp', '.par': 'text/plain-bas', '.paw':
                           'application/vnd.pawaafile', '.fbs': 'image/vnd.fastbidsheet',
                       '.dcurl': 'text/vnd.curl.dcurl', '.gim':
                           'application/vnd.groove-identity-message', '.kfo': 'application/vnd.kde.kformula',
                       '.gif': 'image/gif', '.lrm':
                           'application/vnd.ms-lrm', '.cdkey': 'application/vnd.mediastation.cdkey',
                       '.atomcat': 'application/atomcat+xml',
                       '.i2g': 'application/vnd.intergeo', '.djvu': 'image/vnd.djvu', '.rtf': 'application/rtf',
                       '.xhtml':
                           'application/xhtml+xml', '.azw': 'application/vnd.amazon.ebook',
                       '.wmls': 'text/vnd.wap.wmlscript', '.azs':
                           'application/vnd.airzip.filesecure.azs', '.kon': 'application/vnd.kde.kontour', '.ngdat':
                           'application/vnd.nokia.n-gage.data', '.azf': 'application/vnd.airzip.filesecure.azf',
                       '.wbxml':
                           'application/vnd.wap.wbxml', '.mathml': 'application/mathml+xml',
                       '.vcd': 'application/x-cdlink', '.vcg':
                           'application/vnd.groove-vcard', '.vcf': 'text/x-vcard', '.json': 'application/json',
                       '.shf': 'application/shf+xml',
                       '.grv': 'application/vnd.groove-injector', '.tpt': 'application/vnd.trid.tpt', '.psb':
                           'application/vnd.3gpp.pic-bw-small', '.vcs': 'text/x-vcalendar',
                       '.psf': 'application/x-font-linux-psf', '.tpl':
                           'application/vnd.groove-tool-template', '.htke': 'application/vnd.kenameaapp',
                       '.vcx': 'application/vnd.vcx',
                       '.tiff': 'image/tiff', '.cdmio': 'application/cdmi-object',
                       '.odf': 'application/vnd.oasis.opendocument.formula',
                       '.oda': 'application/oda', '.ustar': 'application/x-ustar',
                       '.odc': 'application/vnd.oasis.opendocument.chart',
                       '.odb': 'application/vnd.oasis.opendocument.database', '.m3u8': 'application/vnd.apple.mpegurl',
                       '.cdmid':
                           'application/cdmi-domain', '.see': 'application/vnd.seemail',
                       '.cdmia': 'application/cdmi-capability', '.fcs':
                           'application/vnd.isac.fcs', '.mpkg': 'application/vnd.apple.installer+xml', '.odt':
                           'application/vnd.oasis.opendocument.text', '.3g2': 'video/3gpp2', '.odp':
                           'application/vnd.oasis.opendocument.presentation',
                       '.ods': 'application/vnd.oasis.opendocument.spreadsheet',
                       '.cdmiq': 'application/cdmi-queue', '.mpn': 'application/vnd.mophun.application', '.mpm':
                           'application/vnd.blueice.multipass', '.mpc': 'application/vnd.mophun.certificate',
                       '.xdssc': 'application/dssc+xml',
                       '.mpy': 'application/vnd.ibm.minipay', '.g3': 'image/g3fax', '.tfi': 'application/thraud+xml',
                       '.mpp':
                           'application/vnd.ms-project', '.tfm': 'application/x-tex-tfm',
                       '.xspf': 'application/xspf+xml', '.nsf':
                           'application/vnd.lotus-notes', '.wmlc': 'application/vnd.wap.wmlc',
                       '.ggb': 'application/vnd.geogebra.file',
                       '.webp': 'image/webp', '.setreg': 'application/set-registration-initiation',
                       '.dpg': 'application/vnd.dpgraph',
                       '.dra': 'audio/vnd.dra', '.ggt': 'application/vnd.geogebra.tool',
                       '.onetoc': 'application/onenote', '.webm':
                           'video/webm', '.sv4cpio': 'application/x-sv4cpio', '.karbon': 'application/vnd.kde.karbon',
                       '.plc':
                           'application/vnd.mobius.plc', '.weba': 'audio/webm', '.jnlp': 'application/x-java-jnlp-file',
                       '.ivp':
                           'application/vnd.immervision-ivp', '.ivu': 'application/vnd.immervision-ivu', '.sldx':
                           'application/vnd.openxmlformats-officedocument.presentationml.slide',
                       '.yang': 'application/yang', '.m4v':
                           'video/x-m4v', '.gv': 'text/vnd.graphviz', '.swf': 'application/x-shockwave-flash', '.swi':
                           'application/vnd.aristanetworks.swi', '.dtshd': 'audio/vnd.dts.hd',
                       '.pfa': 'application/x-font-type1', '.mp4':
                           'application/mp4', '.hvp': 'application/vnd.yamaha.hv-voice',
                       '.rm': 'application/vnd.rn-realmedia', '.hvs':
                           'application/vnd.yamaha.hv-script', '.src': 'application/x-wais-source',
                       '.sbml': 'application/sbml+xml', '.seed':
                           'application/vnd.fdsn.seed', '.zaz': 'application/vnd.zzazz.deck+xml',
                       '.hvd': 'application/vnd.yamaha.hv-dic',
                       '.cmdf': 'chemical/x-cmdf', '.qt': 'video/quicktime', '.sxd': 'application/vnd.sun.xml.draw',
                       '.rs':
                           'application/rls-services+xml',
                       '.ppam': 'application/vnd.ms-powerpoint.addin.macroenabled.12', '.rq':
                           'application/sparql-query', '.rdz': 'application/vnd.data-vision.rdz',
                       '.xop': 'application/xop+xml', '.xdf':
                           'application/xcap-diff+xml', '.h263': 'video/h263', '.cod': 'application/vnd.rim.cod',
                       '.h261': 'video/h261',
                       '.osfpvg': 'application/vnd.yamaha.openscoreformat.osfpvg+xml', '.h264': 'video/h264', '.wpd':
                           'application/vnd.wordperfect', '.skp': 'application/vnd.koan',
                       '.lvp': 'audio/vnd.lucent.voice', '.hqx':
                           'application/mac-binhex40', '.ttl': 'text/turtle', '.ksp': 'application/vnd.kde.kspread',
                       '.sit':
                           'application/x-stuffit', '.doc': 'application/msword', '.uu': 'text/x-uuencode',
                       '.wps': 'application/vnd.ms-works',
                       '.shar': 'application/x-shar', '.psd': 'image/vnd.adobe.photoshop',
                       '.ptid': 'application/vnd.pvi.ptid1', '.cdy':
                           'application/vnd.cinderella', '.cdx': 'chemical/x-cdx', '.slt': 'application/vnd.epson.salt',
                       '.fvt':
                           'video/vnd.fvt', '.ics': 'text/calendar', '.qps': 'application/vnd.publishare-delta-tree',
                       '.ico': 'image/x-icon',
                       '.uoml': 'application/vnd.uoml+xml', '.icc': 'application/vnd.iccprofile',
                       '.ktz': 'application/vnd.kahootz',
                       '.ice': 'x-conference/x-cooltalk', '.ai': 'application/postscript',
                       '.cdbcmsg': 'application/vnd.contact.cmsg',
                       '.esf': 'application/vnd.epson.esf', '.abw': 'application/x-abiword',
                       '.wspolicy': 'application/wspolicy+xml',
                       '.mpga': 'audio/mpeg', '.epub': 'application/epub+zip', '.pki': 'application/pkixcmp',
                       '.hdf': 'application/x-hdf',
                       '.davmount': 'application/davmount+xml', '.thmx': 'application/vnd.ms-officetheme', '.vxml':
                           'application/voicexml+xml', '.bdm': 'application/vnd.syncml.dm+wbxml',
                       '.wqd': 'application/vnd.wqd', '.srx':
                           'application/sparql-results+xml', '.box': 'application/vnd.previewsystems.box',
                       '.sru': 'application/sru+xml',
                       '.oxt': 'application/vnd.openofficeorg.extension', '.pbd': 'application/vnd.powerbuilder6',
                       '.bh2':
                           'application/vnd.fujitsu.oasysprs', '.mxml': 'application/xv+xml', '.dts': 'audio/vnd.dts',
                       '.es3':
                           'application/vnd.eszigno3+xml', '.qbo': 'application/vnd.intu.qbo',
                       '.msty': 'application/vnd.muvee.style', '.odft':
                           'application/vnd.oasis.opendocument.formula-template', '.dtd': 'application/xml-dtd', '.dtb':
                           'application/x-dtbook+xml', '.pclxl': 'application/vnd.hp-pclxl',
                       '.xdp': 'application/vnd.adobe.xdp+xml', '.xdw':
                           'application/vnd.fujixerox.docuworks', '.mbk': 'application/vnd.mobius.mbk', '.cdxml':
                           'application/vnd.chemdraw+xml', '.ipk': 'application/vnd.shana.informed.package', '.org':
                           'application/vnd.lotus-organizer', '.xslt': 'application/xslt+xml', '.apk':
                           'application/vnd.android.package-archive', '.p8': 'application/pkcs8',
                       '.gqf': 'application/vnd.grafeq', '.flx':
                           'text/vnd.fmi.flexstor', '.fly': 'text/vnd.fly', '.kne': 'application/vnd.kinar', '.edx':
                           'application/vnd.novadigm.edx', '.flv': 'video/x-flv', '.flw': 'application/vnd.kde.kivio',
                       '.odg':
                           'application/vnd.oasis.opendocument.graphics', '.ez3': 'application/vnd.ezpix-package',
                       '.ez2':
                           'application/vnd.ezpix-album', '.fli': 'video/x-fli',
                       '.nbp': 'application/vnd.wolfram.player', '.hbci':
                           'application/vnd.hbci', '.pkipath': 'application/pkix-pkipath',
                       '.ssml': 'application/ssml+xml', '.sema':
                           'application/vnd.sema', '.ppt': 'application/vnd.ms-powerpoint', '.png': 'image/png', '.odm':
                           'application/vnd.oasis.opendocument.text-master', '.ppm': 'image/x-portable-pixmap',
                       '.latex':
                           'application/x-latex', '.semd': 'application/vnd.semd', '.ppd': 'application/vnd.cups-ppd',
                       '.cgm': 'image/cgm',
                       '.xfdl': 'application/vnd.xfdl', '.vis': 'application/vnd.visionary',
                       '.igl': 'application/vnd.igloader', '.mbox':
                           'application/mbox', '.semf': 'application/vnd.semf',
                       '.odi': 'application/vnd.oasis.opendocument.image', '.oti':
                           'application/vnd.oasis.opendocument.image-template', '.cdmic': 'application/cdmi-container',
                       '.igx':
                           'application/vnd.micrografx.igx', '.kwd': 'application/vnd.kde.kword', '.igs': 'model/iges',
                       '.apr':
                           'application/vnd.lotus-approach', '.n-gage': 'application/vnd.nokia.n-gage.symbian.install',
                       '.jad':
                           'text/vnd.sun.j2me.app-descriptor', '.mwf': 'application/vnd.mfer',
                       '".rss': 'application/rss+xml', '.npx':
                           'image/vnd.net-fpx', '.jam': 'application/vnd.jam', '.rlc': 'image/vnd.fujixerox.edmics-rlc',
                       '.rld':
                           'application/resource-lists-diff+xml', '.oth': 'application/vnd.oasis.opendocument.text-web',
                       '.bz2':
                           'application/x-bzip2', '.xar': 'application/vnd.xara', '.jar': 'application/java-archive',
                       '.oga': 'audio/ogg',
                       '.afp': 'application/vnd.ibm.modcap', '.application': 'application/x-ms-application',
                       '.mxf': 'application/mxf',
                       '.rgb': 'image/x-rgb', '.mxl': 'application/vnd.recordare.musicxml',
                       '.mxs': 'application/vnd.triscape.mxs', '.ufd':
                           'application/vnd.ufdl', '.gram': 'application/srgs', '.jlt': 'application/vnd.hp-jlyt',
                       '.mxu': 'video/vnd.mpegurl',
                       '.ma': 'application/mathematica', '.qam': 'application/vnd.epson.quickanime', '.pcurl':
                           'application/vnd.curl.pcurl', '.ser': 'application/java-serialized-object', '.portpkg':
                           'application/vnd.macports.portpkg', '.vsf': 'application/vnd.vsf',
                       '.pgp': 'application/pgp-signature', '.xlsb':
                           'application/vnd.ms-excel.sheet.binary.macroenabled.12',
                       '.nlu': 'application/vnd.neurolanguage.nlu', '.pgm':
                           'image/x-portable-graymap', '.xyz': 'chemical/x-xyz', '.svg': 'image/svg+xml',
                       '.svd': 'application/vnd.svd', '.dp':
                           'application/vnd.osgi.dp', '.unityweb': 'application/vnd.unity', '.xlsm':
                           'application/vnd.ms-excel.sheet.macroenabled.12', '.xbap': 'application/x-ms-xbap',
                       '.uva': 'audio/vnd.dece.audio',
                       '.uvm': 'video/vnd.dece.mobile', '.ogx': 'application/ogg', '.uvi': 'image/vnd.dece.graphic',
                       '.uvh':
                           'video/vnd.dece.hd', '.eol': 'audio/vnd.digital-winds',
                       '.cat': 'application/vnd.ms-pki.seccat', '.uvu':
                           'video/vnd.uvvu.mp4', '.uvv': 'video/vnd.dece.video', '.uvp': 'video/vnd.dece.pd', '.eot':
                           'application/vnd.ms-fontobject', '.mag': 'application/vnd.ecowin.chart',
                       '.pya': 'audio/vnd.ms-playready.media.pya',
                       '.iif': 'application/vnd.shana.informed.interchange',
                       '.atx': 'application/vnd.antix.game-component', '.mny':
                           'application/x-msmoney', '.ghf': 'application/vnd.groove-help',
                       '.cpio': 'application/x-cpio', '.pyv':
                           'video/vnd.ms-playready.media.pyv', '.atc': 'application/vnd.acucorp',
                       '.xdm': 'application/vnd.syncml.dm+xml',
                       '.rif': 'application/reginfo+xml', '.scq': 'application/scvp-cv-request',
                       '.scs': 'application/scvp-cv-response',
                       '.scm': 'application/vnd.lotus-screencam', '.scurl': 'text/vnd.curl.scurl',
                       '.rip': 'audio/vnd.rip', '.scd':
                           'application/x-msschedule', '.xfdf': 'application/vnd.adobe.xfdf',
                       '.xwd': 'image/x-xwindowdump', '.xlam':
                           'application/vnd.ms-excel.addin.macroenabled.12', '.aab': 'application/x-authorware-bin',
                       '.aac': 'audio/x-aac',
                       '.sda': 'application/vnd.stardivision.draw', '.aam': 'application/x-authorware-map', '.sdc':
                           'application/vnd.stardivision.calc', '.sdd': 'application/vnd.stardivision.impress', '.rp9':
                           'application/vnd.cloanto.rp9', '.js': 'application/javascript',
                       '.aas': 'application/x-authorware-seg', '.sdp':
                           'application/sdp', '.sdw': 'application/vnd.stardivision.writer',
                       '.plb': 'application/vnd.3gpp.pic-bw-large',
                       '.mscml': 'application/mediaservercontrol+xml', '.plf': 'application/vnd.pocketlearn', '.3dml':
                           'text/vnd.in3d.3dml', '.edm': 'application/vnd.novadigm.edm',
                       '.wtb': 'application/vnd.webturbo', '.msf':
                           'application/vnd.epson.msf', '.pls': 'application/pls+xml',
                       '.flo': 'application/vnd.micrografx.flo', '.msl':
                           'application/vnd.mobius.msl', '.qxd': 'application/vnd.quark.quarkxpress',
                       '.msh': 'model/mesh', '.pcf':
                           'application/x-font-pcf', '.potm': 'application/vnd.ms-powerpoint.template.macroenabled.12',
                       '.7z':
                           'application/x-7z-compressed', '.pcl': 'application/vnd.hp-pcl',
                       '.cpt': 'application/mac-compactpro', '.mdb':
                           'application/x-msaccess', '.cmp': 'application/vnd.yellowriver-custom-menu', '.potx':
                           'application/vnd.openxmlformats-officedocument.presentationml.template', '.jpm': 'video/jpm',
                       '.pcx': 'image/x-pcx',
                       '.zir': 'application/vnd.zul', '.mdi': 'image/vnd.ms-modi', '.zip': 'application/zip',
                       '.m3u': 'audio/x-mpegurl',
                       '.clkk': 'application/vnd.crick.clicker.keyboard', '.ppsx':
                           'application/vnd.openxmlformats-officedocument.presentationml.slideshow',
                       '.class': 'application/java-vm', '.mpeg':
                           'video/mpeg', '.mmf': 'application/vnd.smaf', '.mj2': 'video/mj2',
                       '.xer': 'application/patch-ops-error+xml',
                       '.asf': 'video/x-ms-asf', '.vsd': 'application/vnd.visio',
                       '.clkx': 'application/vnd.crick.clicker', '.clkw':
                           'application/vnd.crick.clicker.wordbank', '.xo': 'application/vnd.olpc-sugar', '.clkt':
                           'application/vnd.crick.clicker.template', '.aso': 'application/vnd.accpac.simply.aso',
                       '.mmr':
                           'image/vnd.fujixerox.edmics-mmr', '.clkp': 'application/vnd.crick.clicker.palette',
                       '.sh': 'application/x-sh',
                       '.sm': 'application/vnd.stepmania.stepchart', '.wbs': 'application/vnd.criticaltools.wbs+xml',
                       '.sc':
                           'application/vnd.ibm.secure-container', '.cif': 'chemical/x-cif',
                       '.xls': 'application/vnd.ms-excel', '.cii':
                           'application/vnd.anser-web-certificate-issue-initiation',
                       '.st': 'application/vnd.sailingtracker.track', '.cil':
                           'application/vnd.ms-artgalry', '.3gp': 'video/3gpp', '.gtw': 'model/vnd.gtw', '.gtm':
                           'application/vnd.groove-tool-message', '.trm': 'application/x-msterminal', '.ppsm':
                           'application/vnd.ms-powerpoint.slideshow.macroenabled.12',
                       '.pub': 'application/x-mspublisher', '.html':
                           'text/html', '.ims': 'application/vnd.ms-ims', '.tra': 'application/vnd.trueapp', '.fsc':
                           'application/vnd.fsc.weblaunch', '.ifm': 'application/vnd.shana.informed.formdata',
                       '.wgt': 'application/widget',
                       '.sgl': 'application/vnd.stardivision.writer-global',
                       '.musicxml': 'application/vnd.recordare.musicxml+xml', '.lbd':
                           'application/vnd.llamagraphics.life-balance.desktop', '.lbe':
                           'application/vnd.llamagraphics.life-balance.exchange+xml', '.fst': 'image/vnd.fst',
                       '.n3': 'text/n3', '.woff':
                           'application/x-font-woff', '.sgml': 'text/sgml', '.mvb': 'application/x-msmediaview', '.les':
                           'application/vnd.hhe.lesson-player', '.rms': 'application/vnd.jcp.javame.midlet-rms',
                       '.mets':
                           'application/mets+xml', '.rmp': 'audio/x-pn-realaudio-plugin', '.rdf': 'application/rdf+xml',
                       'java"':
                           '"text/x-java-source', '.sxw': 'application/vnd.sun.xml.writer',
                       '.spot': 'text/vnd.in3d.spot', '.nc':
                           'application/x-netcdf', '.fzs': 'application/vnd.fuzzysheet',
                       '.sxm': 'application/vnd.sun.xml.math', '.mseq':
                           'application/vnd.mseq', '.setpay': 'application/set-payment-initiation',
                       '.sxi': 'application/vnd.sun.xml.impress',
                       '.aep': 'application/vnd.audiograph', '.bin': 'application/octet-stream', '.sxg':
                           'application/vnd.sun.xml.writer.global', '0.123': 'application/vnd.lotus-1-2-3', '.sxc':
                           'application/vnd.sun.xml.calc', '.ac': 'application/pkix-attr-cert', '.pptm':
                           'application/vnd.ms-powerpoint.presentation.macroenabled.12',
                       '.itp': 'application/vnd.shana.informed.formtemplate',
                       '.xltm': 'application/vnd.ms-excel.template.macroenabled.12', '.c': 'text/x-c', '.rcprofile':
                           'application/vnd.ipunplugged.rcprofile', '.f': 'text/x-fortran', '.fe_launch':
                           'application/vnd.denovo.fcselayout-link', '.vtu': 'model/vnd.vtu', '.xltx':
                           'application/vnd.openxmlformats-officedocument.spreadsheetml.template',
                       '.aw': 'application/applixware', '.pptx':
                           'application/vnd.openxmlformats-officedocument.presentationml.presentation',
                       '.p': 'text/x-pascal', '.s':
                           'text/x-asm', '.t': 'text/troff', '.wpl': 'application/vnd.ms-wpl',
                       '.xenc': 'application/xenc+xml', '.btif':
                           'image/prs.btif', '.gnumeric': 'application/x-gnumeric', '.mods': 'application/mods+xml',
                       '.docm':
                           'application/vnd.ms-word.document.macroenabled.12', '.nnw': 'application/vnd.noblenet-web',
                       '.x3d':
                           'application/vnd.hzn-3d-crossword', '.xap': 'application/x-silverlight-app',
                       '.igm': 'application/vnd.insors.igm',
                       '.pfr': 'application/font-tdpfr', '.docx':
                           'application/vnd.openxmlformats-officedocument.wordprocessingml.document', '.zmm':
                           'application/vnd.handheld-entertainment+xml', '.sv4crc': 'application/x-sv4crc', '.cmc':
                           'application/vnd.cosmocaller', '.cml': 'chemical/x-cml',
                       '.pvb': 'application/vnd.3gpp.pic-bw-var', '.mgz':
                           'application/vnd.proteus.magazine', '.au': 'audio/basic', '.mid': 'audio/midi',
                       '.mif': 'application/vnd.mif',
                       '.chat': 'application/x-chat', '.cmx': 'image/x-cmx',
                       '.kml': 'application/vnd.google-earth.kml+xml', '.jpgv':
                           'video/jpeg', '.gph': 'application/vnd.flographit',
                       '.sfd-hdstx': 'application/vnd.hydrostatix.sof-data', '.ncx':
                           'application/x-dtbncx+xml', '.wg': 'application/vnd.pmi.widget',
                       '.kmz': 'application/vnd.google-earth.kmz', '.wm':
                           'video/x-ms-wm', '.teacher': 'application/vnd.smart.teacher',
                       '.dis': 'application/vnd.mobius.dis', '.dir':
                           'application/x-director', '.curl': 'text/vnd.curl',
                       '.sldm': 'application/vnd.ms-powerpoint.slide.macroenabled.12',
                       '.snf': 'application/x-font-snf', '.mmd': 'application/vnd.chipnuts.karaoke-mmd', '.lasxml':
                           'application/vnd.las.las+xml', '.ftc': 'application/vnd.fluxtime.clip', '.fti':
                           'application/vnd.anser-web-funds-transfer-initiation', '.mads': 'application/mads+xml'}
