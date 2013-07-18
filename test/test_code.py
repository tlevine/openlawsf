# vim: set fileencoding=utf-8 :
import nose.tools as n
from lxml.html import fromstring

import lib

html = fromstring(u'''
<div id="ref_id" style="display: none">California/San Francisco Building Inspection Commission (BIC) Codes/ CITY AND COUNTY OF SAN FRANCISCO BUILDING INDUSTRY COMMISSION (BIC) CODES </div>
<link rel="stylesheet" type="text/css" href="/nxt/gateway.dll/California/sfbuilding/cityandcountyofsanfranciscobuildingindus?f=stylesheets$fn=ALP_style.css$3.0" />

<style>
	@media screen {
		div.new_window {
			text-align: right;
		}
	}
	@media print {
		div.new_window, div#refbox {
			display: none;
		}
	}
	a.new_window {
		font-size: 8pt;
		font-family: Arial;
		color: #6D779E;
	}
	body {
		margin-top: 0;
	}
	.showurl {
		text-decoration: none;
	}
</style>

<script type="text/javascript">
	var ref = document.getElementById("ref_id").innerHTML;

	function openWindow()
	{
		var win_name = "window" + new Date().getTime();
//		var new_win = window.open("/nxt/gateway.dll/California/sfbuilding/cityandcountyofsanfranciscobuildingindus?f=templates$fn=document-frameset.htm$3.0", win_name, "resizable=yes,scrollbars=yes,top=0,left=0,width=" + parseInt(screen.availWidth * .75) + ",height=" + parseInt(screen.availHeight *.75));
		var new_win = window.open("/nxt/gateway.dll/California/sfbuilding/cityandcountyofsanfranciscobuildingindus?f=templates$fn=default.htm$3.0", win_name, "resizable=yes,scrollbars=yes,top=0,left=0,width=" + parseInt(screen.availWidth * .75) + ",height=" + parseInt(screen.availHeight *.75));
	}
</script>


<!DOCTYPE HTML PUBLIC "-//W3C//DTD W3 HTML//EN">
<HTML>
<HEAD>
<script language="JavaScript">
  var nextyear = new Date();
  nextyear.setFullYear(nextyear.getFullYear() + 1);
  var PathExp = "; path=/; expires=" + nextyear.toGMTString();
  var Off = document.cookie.indexOf("name=RL:0");
  var On = document.cookie.indexOf("name=RL:1");

  document.writeln('<style type="text/css">');
  if (Off != -1) {
    //if (navigator.appName == "Netscape") {
	  //document.classes.refline.all.display = "normal";
	//} else {
	  document.writeln('td.refline {display:normal}');
	//}
  } else {
    if (On != -1) {
      //if (navigator.appName == "Netscape") {
		//document.classes.refline.all.display = "normal";
      //} else {
	    document.writeln('td.refline {display:normal}');
      //}
    } else {
      document.cookie = "name=RL:0" + PathExp;
      //if (navigator.appName == "Netscape") {
		//document.classes.refline.all.display = "normal";
	  //} else {
	    document.writeln('td.refline {display:normal}');
	  //}
    }
  }
  document.writeln('</style>');


  function switchit() {
    if (navigator.appName == "Netscape") {
	  if (document.forms.ChangeBox.ShowStyleBox.checked == 1) {
	    document.cookie = "name=RL:1" + PathExp;
      } else {
	    document.cookie = "name=RL:0" + PathExp;
	  }
    } else {
        if (ChangeBox.ShowStyleBox.checked == 1) {
          document.cookie = "name=RL:1" + PathExp;
        } else {
          document.cookie = "name=RL:0" + PathExp;
        }
    }
	location.reload();
  }

</script>

	<LINK rel="stylesheet" href="/nxt/gateway.dll?f=id$id=sfbuilding.css$t=document-frame.htm$3.0$p=" type="text/css">
<script type="text/javascript" src="/alp_templates/url.js"></script>
</HEAD>
<BODY bgColor=#ffffff>
<form style="margin-bottom:1px;margin-bottom:1px" name="ChangeBox">
<table border="1" width="100%" cellspacing="0" cellpadding="0" style="background-color: #ffffff">
<tr><td>
<p style="margin-bottom:1px;margin-bottom:1px;text-align:center"><span style="font-family:Arial;font-size:8pt"> San Francisco Building Inspection Commission (BIC) Codes</span></p>
</td></tr>
<tr><td class="refline" bgcolor="#d3d3d3">
<p class="refline" style="margin-left:1px;"><a href="/nxt/gateway.dll?f=id$id=San%20Francisco%20Building%20Inspection%20Commission%20(BIC)%20Codes%3Ar%3A1$t=document-frame.htm$3.0$p=" class="refline"> CITY AND COUNTY OF SAN FRANCISCO BUILDING INDUSTRY COMMISSION (BIC) CODES </a></p>
</td></tr>
</table>
</form>
<META http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<BR />
<A NAME='JD_SFBIC'></A>
<H1 CLASS='Code'><a href="javascript:void(0)" onclick="showUrl('')"><img src="/alp_templates/images/ui-bookmark.gif" width="16" height="16" alt="Bookmark" border="0"></a><span href="javascript:void(0)" onclick="showUrl('')" style="cursor: pointer">CITY AND COUNTY OF SAN FRANCISCO<BR />
BUILDING INDUSTRY COMMISSION (BIC) CODES<BR />
</span></H1>
<P CLASS='Introduction'><FONT SIZE=5><B>BUILDING, ELECTRICAL, HOUSING,<BR />
MECHANICAL AND PLUMBING CODES<BR />
</B></FONT></P>
<P CLASS='Introduction'><B>The San Francisco Building Industry Commission (BIC) Codes contain:<BR />
Ordinances approved through April 9, 2013 and<BR />
Administrative Bulletins approved through April 3, 2013.<BR />
</B></P>
<P CLASS='Introduction'><IMG SRC='/nxt/gateway.dll?f=id$id=San%20Francisco%20Building%20Inspection%20Commission%20(BIC)%20Codes%3Ao%3A24$cid=california$t=document-frame.htm$3.0$p=' BORDER=0 WIDTH=216 HEIGHT=200></P>
<TABLE CELLPADDING=0 CELLSPACING=0 BORDER=0 WIDTH='100%'><TR><TD ALIGN=CENTER>
<TABLE CELLSPACING=0 BORDER=1 BORDERCOLOR=#C0C0C0 RULES=ALL WIDTH=576 CELLPADDING=4>
<TR><TD COLSPAN=3 WIDTH=576 VALIGN=TOP BGCOLOR=#C0C0C0><P CLASS='CodeListHeader'>The San Francisco Municipal Code:</P>
</TD></TR>
<TR><TD WIDTH=192 VALIGN=TOP><P CLASS='CodeList'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Charter%3Ar%3A2$cid=california$t=document-frame.htm$an=JD_Charter$3.0#JD_Charter'>Charter</A></P>
<P CLASS='CodeList'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Administrative%20Code%3Ar%3A2$cid=california$t=document-frame.htm$an=JD_Administrative$3.0#JD_Administrative'>Administrative Code</A></P>
<P CLASS='CodeList'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Building%20Inspection%20Commission%20(BIC)%20Codes%3Ar%3A1$cid=california$t=document-frame.htm$an=JD_SFBIC$3.0#JD_SFBIC'>Building, Electrical, Housing, Mechanical and Plumbing Codes</A></P>
<P CLASS='CodeList'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A2$cid=california$t=document-frame.htm$an=JD_Business$3.0#JD_Business'>Business and Tax Regulations Code</A></P>
<P CLASS='CodeList'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Campaign%20and%20Governmental%20Conduct%20Code%3Ar%3A2$cid=california$t=document-frame.htm$an=JD_Campaign$3.0#JD_Campaign'>Campaign and Governmental Conduct Code</A></P>
</TD><TD WIDTH=192 VALIGN=TOP><P CLASS='CodeList'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Environment%20Code%3Ar%3A2$cid=california$t=document-frame.htm$an=JD_Environment$3.0#JD_Environment'>Environment Code</A></P>
<P CLASS='CodeList'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Fire%20Code%3Ar%3A2$cid=california$t=document-frame.htm$an=JD_Fire$3.0#JD_Fire'>Fire Code</A></P>
<P CLASS='CodeList'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Health%20Code%3Ar%3A2$cid=california$t=document-frame.htm$an=JD_Health$3.0#JD_Health'>Health Code</A></P>
<P CLASS='CodeList'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Municipal%20Elections%20Code%3Ar%3A2$cid=california$t=document-frame.htm$an=JD_Elections$3.0#JD_Elections'>Municipal Elections Code</A></P>
<P CLASS='CodeList'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Park%20Code%3Ar%3A2$cid=california$t=document-frame.htm$an=JD_Park$3.0#JD_Park'>Park Code</A></P>
<P CLASS='CodeList'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Planning%20Code%3Ar%3A4553$cid=california$t=document-frame.htm$an=JD_Planning$3.0#JD_Planning'>Planning Code</A></P>
<P CLASS='CodeList'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Police%20Code%3Ar%3A2$cid=california$t=document-frame.htm$an=JD_Police$3.0#JD_Police'>Police Code</A></P>
</TD><TD WIDTH=192 VALIGN=TOP><P CLASS='CodeList'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Port%20Code%3Ar%3A2$cid=california$t=document-frame.htm$an=JD_Port$3.0#JD_Port'>Port Code</A></P>
<P CLASS='CodeList'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Public%20Works%20Code%3Ar%3A2$cid=california$t=document-frame.htm$an=JD_PublicWorks$3.0#JD_PublicWorks'>Public Works Code</A></P>
<P CLASS='CodeList'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Subdivision%20Code%3Ar%3A2$cid=california$t=document-frame.htm$an=JD_Subdivision$3.0#JD_Subdivision'>Subdivision Code</A></P>
<P CLASS='CodeList'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Transportation%20Code%3Ar%3A2$cid=california$t=document-frame.htm$an=JD_Transportation$3.0#JD_Transportation'>Transportation Code</A></P>
<P CLASS='CodeList'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Zoning%20Maps%3Ar%3A153$cid=california$t=document-frame.htm$an=JD_ZoningMaps$3.0#JD_ZoningMaps'>Zoning Maps</A></P>
<P CLASS='CodeList'>
<A HREF='/nxt/gateway.dll?f=id$id=Comprehensive%20Ordinance%20List%3Ar%3A2$cid=california$t=document-frame.htm$an=JD_OrdTable$3.0#JD_OrdTable'>Comprehensive Ordinance Table</A></P>
</TD></TR></TABLE>
</TD></TR></TABLE>
<P CLASS='Introduction'><B>AMERICAN LEGAL PUBLISHING CORPORATION<BR />
</B>432 Walnut Street, Suite 1200<BR />
Cincinnati, Ohio  45202-3909<BR />
(800) 445-5588<BR />
Fax: (513) 763-3562<BR />
Email: <A HREF='mailto:customerservice@amlegal.com'>customerservice@amlegal.com</A><BR />
<A HREF='http://www.amlegal.com' TARGET="_blank">www.amlegal.com</A></P>


<div style="text-align: left; color: #6D779E; font-family: Arial, Helvetica, sans-serif; font-size: 8pt">
<b><u>Disclaimer:</u></b><br>

This Code of Ordinances and/or any other documents that appear on this site may not reflect the most current legislation adopted by the Municipality.  American Legal Publishing Corporation provides these documents for informational purposes only. These documents should not be relied upon as the definitive authority for local legislation. Additionally, the formatting and pagination of the posted documents varies from the formatting and pagination of the official copy.  The official printed copy of a Code of Ordinances should be consulted prior to any action being taken.<br><br>

For further information regarding the official version of any of this Code of Ordinances or other documents posted on this site, please contact the Municipality directly or contact American Legal Publishing toll-free at 800-445-5588.<br><br>

<center>
&copy; 2013 American Legal Publishing Corporation<br>
<a href="mailto:techsupport@amlegal.com">techsupport@amlegal.com</a><br>
1.800.445.5588.<br>
</center>
</div>
</BODY>
</HTML>
<form name="LPHitCountForm">
<input type="hidden" name="LPHitCount" value="0">
</form>
''')
observed = len(lib.codes(html))

def test_count():
    'The list of codes should have the correct length.'
    expected = 18
    n.assert_equal(observed, expected)
