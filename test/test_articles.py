# vim: set fileencoding=utf-8 :
import nose.tools as n
from lxml.html import fromstring

import lib
html = fromstring('''
<div id="ref_id" style="display: none">California/San Francisco Business and Tax Regulations Code/BUSINESS AND TAX REGULATIONS CODE</div>
<link rel="stylesheet" type="text/css" href="/nxt/gateway.dll/California/business/businessandtaxregulationscode?f=stylesheets$fn=ALP_style.css$3.0" />

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
//		var new_win = window.open("/nxt/gateway.dll/California/business/businessandtaxregulationscode?f=templates$fn=document-frameset.htm$3.0", win_name, "resizable=yes,scrollbars=yes,top=0,left=0,width=" + parseInt(screen.availWidth * .75) + ",height=" + parseInt(screen.availHeight *.75));
var new_win = window.open("/nxt/gateway.dll/California/business/businessandtaxregulationscode?f=templates$fn=default.htm$3.0", win_name, "resizable=yes,scrollbars=yes,top=0,left=0,width=" + parseInt(screen.availWidth * .75) + ",height=" + parseInt(screen.availHeight *.75));
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

<LINK rel="stylesheet" href="/nxt/gateway.dll?f=id$id=business.css$t=document-frame.htm$3.0$p=" type="text/css">
<script type="text/javascript" src="/alp_templates/url.js"></script>
</HEAD>
<BODY bgColor=#ffffff>
<form style="margin-bottom:1px;margin-bottom:1px" name="ChangeBox">
<table border="1" width="100%" cellspacing="0" cellpadding="0" style="background-color: #ffffff">
<tr><td>
<p style="margin-bottom:1px;margin-bottom:1px;text-align:center"><span style="font-family:Arial;font-size:8pt"> San Francisco Business and Tax Regulations Code</span></p>
</td></tr>
<tr><td class="refline" bgcolor="#d3d3d3">
<p class="refline" style="margin-left:1px;"><a href="/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A2$t=document-frame.htm$3.0$p=" class="refline">BUSINESS AND TAX REGULATIONS CODE</a></p>
</td></tr>
</table>
</form>
<META http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<A NAME='JD_Business'></A>
<H1 CLASS='Article'><a href="javascript:void(0)" onclick="showUrl('')"><img src="/alp_templates/images/ui-bookmark.gif" width="16" height="16" alt="Bookmark" border="0"></a><span href="javascript:void(0)" onclick="showUrl('')" style="cursor: pointer">BUSINESS AND TAX REGULATIONS CODE</span></H1>
<P CLASS='NewOrdNotice'><IMG SRC='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ao%3A29$cid=california$t=document-frame.htm$3.0$p=' BORDER=0 WIDTH=108 HEIGHT=54> New Ordinance Notice</P>
<P CLASS='NewOrdPubNote'><B>Publisher's Note:</B> This Code includes sections affected by new ordinances.
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3Ace9$cid=california$t=document-frame.htm$an=JD_NewOrds$3.0#JD_NewOrds'>Click here</A> for a list of the new ordinances and the affected sections.</P>
<P CLASS='Currency'>The San Francisco Municipal Code is current through <A HREF='http://www.sfbos.org/ftp/uploadedfiles/bdsupvrs/ordinances13/o0107-13.pdf' TARGET="_blank">Ordinance 107-13</A>, File No. 130070, approved June 13, 2013, effective July 13, 2013.</P>
<P CLASS='Currency'>The Business and Tax Regulations Code was last amended by <A HREF='http://www.sfbos.org/ftp/uploadedfiles/bdsupvrs/ordinances13/o0096-13.pdf' TARGET="_blank">Ordinance 96-13</A>, File No. 130244, approved May 31, 2013, effective June 30, 2013.</P>
<P CLASS='CenterBold'><IMG SRC='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ao%3A2b$cid=california$t=document-frame.htm$3.0$p=' BORDER=0 WIDTH=216 HEIGHT=200></P>
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
<P CLASS='Center'><B>AMERICAN LEGAL PUBLISHING CORPORATION<BR />
</B>432 Walnut Street, Suite 1200<BR />
Cincinnati, Ohio  45202-3909<BR />
(800) 445-5588<BR />
Fax: (513) 763-3562<BR />
Email: <A HREF='mailto:customerservice@amlegal.com'>customerservice@amlegal.com</A><BR />
<A HREF='http://www.amlegal.com' TARGET="_blank">www.amlegal.com</A></P>

<a name="LPTOC1"></a><H2 CLASS='Chapter'>PREFACE TO THE<BR />
BUSINESS AND TAX REGULATIONS CODE </H2>
<P>     This electronic version of the City and County of San Francisco Municipal Code is updated as amending legislation is approved. New Ordinance Notices are inserted where applicable to call the user's attention to material that has been affected by legislation that has been passed but is not yet effective. Any references to such legislation are also compiled in a
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3Ace9$cid=california$t=document-frame.htm$an=JD_NewOrds$3.0#JD_NewOrds'>table</A> at the end of this Code. The amendments are then incorporated into the Code when they become effective.</P>
<P>     Beginning with ordinances passed in 2011, all ordinances affecting this Code are summarized in a
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3Ace9$cid=california$t=document-frame.htm$an=JD_PRTable$3.0#JD_PRTable'>table</A> that lists the identifying information (ordinance and file numbers), effective date, short title, and sections affected for each such ordinance. Users should note that the operative date of an ordinance may be later than the effective date of the ordinance. A delayed operative date will be noted in the ordinance.</P>
<P>     This Code may contain various Editor's Notes (explaining the disposition of or cross referencing various provisions), and/or Codification Notes (documenting scrivener's errors and the like found in the underlying ordinances). Such notes have been inserted by the publisher for the convenience of the user or as historical references. They have not been approved or adopted by the City and County of San Francisco, and are of no legal force or effect.</P>
<P><B>Article</B></P>

<TABLE CELLSPACING=0 WIDTH=648 CELLPADDING=4>
<TR><TD WIDTH=72 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3Ae$cid=california$t=document-frame.htm$an=JD_Article1$3.0#JD_Article1'><B>1.</B></A></P>
</TD><TD WIDTH=576 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3Ae$cid=california$t=document-frame.htm$an=JD_Article1$3.0#JD_Article1'>PERMIT PROCEDURES</A></P>
</TD></TR>
<TR><TD WIDTH=72 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A198$cid=california$t=document-frame.htm$an=JD_Article2$3.0#JD_Article2'>2.</A></P>
</TD><TD WIDTH=576 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A198$cid=california$t=document-frame.htm$an=JD_Article2$3.0#JD_Article2'>LICENSE FEES</A></P>
</TD></TR>
<TR><TD WIDTH=72 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A323$cid=california$t=document-frame.htm$an=JD_Article3$3.0#JD_Article3'>3.</A></P>
</TD><TD WIDTH=576 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A323$cid=california$t=document-frame.htm$an=JD_Article3$3.0#JD_Article3'>TRANSIENT MERCHANTS </A></P>
</TD></TR>
<TR><TD WIDTH=72 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A356$cid=california$t=document-frame.htm$an=JD_Article5$3.0#JD_Article5'>5.</A></P>
</TD><TD WIDTH=576 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A356$cid=california$t=document-frame.htm$an=JD_Article5$3.0#JD_Article5'>ELECTRICAL MUSICAL DEVICES</A></P>
</TD></TR>
<TR><TD WIDTH=72 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A3bd$cid=california$t=document-frame.htm$an=JD_Article6$3.0#JD_Article6'>6.</A></P>
</TD><TD WIDTH=576 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A3bd$cid=california$t=document-frame.htm$an=JD_Article6$3.0#JD_Article6'>COMMON ADMINISTRATIVE PROVISIONS </A></P>
</TD></TR>
<TR><TD WIDTH=72 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_Article7$3.0#JD_Article7'>7.</A></P>
</TD><TD WIDTH=576 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_Article7$3.0#JD_Article7'>TAX ON TRANSIENT OCCUPANCY OF HOTEL ROOMS</A></P>
</TD></TR>
<TR><TD WIDTH=72 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A60f$cid=california$t=document-frame.htm$an=JD_Article9$3.0#JD_Article9'>9.</A></P>
</TD><TD WIDTH=576 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A60f$cid=california$t=document-frame.htm$an=JD_Article9$3.0#JD_Article9'>TAX ON OCCUPANCY OF PARKING SPACE IN PARKING STATIONS</A></P>
</TD></TR>
<TR><TD WIDTH=72 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A64a$cid=california$t=document-frame.htm$an=JD_Article10$3.0#JD_Article10'>10.</A></P>
</TD><TD WIDTH=576 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A64a$cid=california$t=document-frame.htm$an=JD_Article10$3.0#JD_Article10'>UTILITY USERS TAX</A></P>
</TD></TR>
<TR><TD WIDTH=72 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A6ce$cid=california$t=document-frame.htm$an=JD_Article10B$3.0#JD_Article10B'>10B.</A></P>
</TD><TD WIDTH=576 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A6ce$cid=california$t=document-frame.htm$an=JD_Article10B$3.0#JD_Article10B'>ACCESS LINE TAX </A></P>
</TD></TR>
<TR><TD WIDTH=72 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A6fb$cid=california$t=document-frame.htm$an=JD_Article11$3.0#JD_Article11'>11.</A></P>
</TD><TD WIDTH=576 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A6fb$cid=california$t=document-frame.htm$an=JD_Article11$3.0#JD_Article11'>STADIUM OPERATOR ADMISSION TAX</A></P>
</TD></TR>
<TR><TD WIDTH=72 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A72d$cid=california$t=document-frame.htm$an=JD_Article12$3.0#JD_Article12'>12.</A></P>
</TD><TD WIDTH=576 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A72d$cid=california$t=document-frame.htm$an=JD_Article12$3.0#JD_Article12'>BUSINESS REGISTRATION </A></P>
</TD></TR>
<TR><TD WIDTH=72 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A7a4$cid=california$t=document-frame.htm$an=JD_Article12-A$3.0#JD_Article12-A'>12-A.</A></P>
</TD><TD WIDTH=576 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A7a4$cid=california$t=document-frame.htm$an=JD_Article12-A$3.0#JD_Article12-A'>PAYROLL EXPENSE TAX ORDINANCE </A></P>
</TD></TR>
<TR><TD WIDTH=72 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A894$cid=california$t=document-frame.htm$an=JD_Article12-B$3.0#JD_Article12-B'>12-B.</A></P>
</TD><TD WIDTH=576 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A894$cid=california$t=document-frame.htm$an=JD_Article12-B$3.0#JD_Article12-B'>BUSINESS TAX REFUND</A></P>
</TD></TR>
<TR><TD WIDTH=72 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A91d$cid=california$t=document-frame.htm$an=JD_Article12B-1$3.0#JD_Article12B-1'>12B-1.</A></P>
</TD><TD WIDTH=576 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A91d$cid=california$t=document-frame.htm$an=JD_Article12B-1$3.0#JD_Article12B-1'>NEIGHBORHOOD BEAUTIFICATION AND GRAFFITI CLEAN-UP FUND TAX OPTION</A></P>
</TD></TR>
<TR><TD WIDTH=72 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A92b$cid=california$t=document-frame.htm$an=JD_Article12-C$3.0#JD_Article12-C'>12-C.</A></P>
</TD><TD WIDTH=576 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A92b$cid=california$t=document-frame.htm$an=JD_Article12-C$3.0#JD_Article12-C'>REAL PROPERTY TRANSFER TAX</A></P>
</TD></TR>
<TR><TD WIDTH=72 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A9de$cid=california$t=document-frame.htm$an=JD_Article12-D$3.0#JD_Article12-D'>12-D.</A></P>
</TD><TD WIDTH=576 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A9de$cid=california$t=document-frame.htm$an=JD_Article12-D$3.0#JD_Article12-D'>UNIFORM LOCAL SALES AND USE TAX</A></P>
</TD></TR>
<TR><TD WIDTH=72 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3Aa26$cid=california$t=document-frame.htm$an=JD_Article13$3.0#JD_Article13'>13.</A></P>
</TD><TD WIDTH=576 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3Aa26$cid=california$t=document-frame.htm$an=JD_Article13$3.0#JD_Article13'>CONNECTIONS TO THE POLICE DEPARTMENT TERMINAL ALARM PANEL</A></P>
</TD></TR>
<TR><TD WIDTH=72 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3Aa69$cid=california$t=document-frame.htm$an=JD_Article14$3.0#JD_Article14'>14.</A></P>
</TD><TD WIDTH=576 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3Aa69$cid=california$t=document-frame.htm$an=JD_Article14$3.0#JD_Article14'>TRANSPORTATION AUTHORITY</A></P>
</TD></TR>
<TR><TD WIDTH=72 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3Aac5$cid=california$t=document-frame.htm$an=JD_Article15$3.0#JD_Article15'>15.</A></P>
</TD><TD WIDTH=576 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3Aac5$cid=california$t=document-frame.htm$an=JD_Article15$3.0#JD_Article15'>BUSINESS IMPROVEMENT DISTRICTS PROCEDURE CODE</A></P>
</TD></TR>
<TR><TD WIDTH=72 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3Ab32$cid=california$t=document-frame.htm$an=JD_Article17$3.0#JD_Article17'>17.</A></P>
</TD><TD WIDTH=576 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3Ab32$cid=california$t=document-frame.htm$an=JD_Article17$3.0#JD_Article17'>BUSINESS TAX PENALTY AMNESTY PROGRAM</A></P>
</TD></TR>
<TR><TD WIDTH=72 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3Ab5b$cid=california$t=document-frame.htm$an=JD_Article20$3.0#JD_Article20'>20.</A></P>
</TD><TD WIDTH=576 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3Ab5b$cid=california$t=document-frame.htm$an=JD_Article20$3.0#JD_Article20'>FINANCIAL INFORMATION PRIVACY ORDINANCE</A></P>
</TD></TR>
<TR><TD WIDTH=72 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3Abd4$cid=california$t=document-frame.htm$an=JD_Article22$3.0#JD_Article22'>22.</A></P>
</TD><TD WIDTH=576 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3Abd4$cid=california$t=document-frame.htm$an=JD_Article22$3.0#JD_Article22'>PARKING STATIONS; REVENUE CONTROL EQUIPMENT</A></P>
</TD></TR>
<TR><TD WIDTH=72 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3Acc9$cid=california$t=document-frame.htm$an=JD_Article23$3.0#JD_Article23'>23.</A></P>
</TD><TD WIDTH=576 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3Acc9$cid=california$t=document-frame.htm$an=JD_Article23$3.0#JD_Article23'>VEHICLE REGISTRATION FEE EXPENDITURE PLAN</A></P>
</TD></TR></TABLE>


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
html.make_links_absolute('http://www.amlegal.com/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A2$cid=california$t=document-frame.htm$an=JD_Business$3.0#JD_Business')
observed = lib.articles(html)


html2 = fromstring('''
<div id="ref_id" style="display: none">California/San Francisco Business and Tax Regulations Code/ARTICLE 23: VEHICLE REGISTRATION FEE EXPENDITURE PLAN</div>
<link rel="stylesheet" type="text/css" href="/nxt/gateway.dll/California/business/article23vehicleregistrationfeeexpenditu?f=stylesheets$fn=ALP_style.css$3.0" />

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
//		var new_win = window.open("/nxt/gateway.dll/California/business/article23vehicleregistrationfeeexpenditu?f=templates$fn=document-frameset.htm$3.0", win_name, "resizable=yes,scrollbars=yes,top=0,left=0,width=" + parseInt(screen.availWidth * .75) + ",height=" + parseInt(screen.availHeight *.75));
		var new_win = window.open("/nxt/gateway.dll/California/business/article23vehicleregistrationfeeexpenditu?f=templates$fn=default.htm$3.0", win_name, "resizable=yes,scrollbars=yes,top=0,left=0,width=" + parseInt(screen.availWidth * .75) + ",height=" + parseInt(screen.availHeight *.75));
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

	<LINK rel="stylesheet" href="/nxt/gateway.dll?f=id$id=business.css$t=document-frame.htm$3.0$p=" type="text/css">
<script type="text/javascript" src="/alp_templates/url.js"></script>
</HEAD>
<BODY bgColor=#ffffff>
<form style="margin-bottom:1px;margin-bottom:1px" name="ChangeBox">
<table border="1" width="100%" cellspacing="0" cellpadding="0" style="background-color: #ffffff">
<tr><td>
<p style="margin-bottom:1px;margin-bottom:1px;text-align:center"><span style="font-family:Arial;font-size:8pt"> San Francisco Business and Tax Regulations Code</span></p>
</td></tr>
<tr><td class="refline" bgcolor="#d3d3d3">
<p class="refline" style="margin-left:1px;"><a href="/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3Acc9$t=document-frame.htm$3.0$p=" class="refline">ARTICLE 23: VEHICLE REGISTRATION FEE EXPENDITURE PLAN</a></p>
</td></tr>
</table>
</form>
<META http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<A NAME='JD_Article23'></A>
<H1 CLASS='Article'><a href="javascript:void(0)" onclick="showUrl('')"><img src="/alp_templates/images/ui-bookmark.gif" width="16" height="16" alt="Bookmark" border="0"></a><span href="javascript:void(0)" onclick="showUrl('')" style="cursor: pointer">ARTICLE 23:<BR />
VEHICLE REGISTRATION FEE EXPENDITURE PLAN</span></H1>

<TABLE CELLSPACING=0 WIDTH=672 CELLPADDING=4>
<TR><TD WIDTH=96 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3Acc9$cid=california$t=document-frame.htm$an=JD_2301$3.0#JD_2301'>Sec. 2301.</A></P>
</TD><TD WIDTH=576 VALIGN=TOP><P CLASS='ChapAn'>Title.</P>
</TD></TR>
<TR><TD WIDTH=96 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3Acc9$cid=california$t=document-frame.htm$an=JD_2302$3.0#JD_2302'>Sec. 2302.</A></P>
</TD><TD WIDTH=576 VALIGN=TOP><P CLASS='ChapAn'>Definitions.</P>
</TD></TR>
<TR><TD WIDTH=96 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3Acc9$cid=california$t=document-frame.htm$an=JD_2303$3.0#JD_2303'>Sec. 2303.</A></P>
</TD><TD WIDTH=576 VALIGN=TOP><P CLASS='ChapAn'>Purpose.</P>
</TD></TR>
<TR><TD WIDTH=96 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3Acc9$cid=california$t=document-frame.htm$an=JD_2304$3.0#JD_2304'>Sec. 2304.</A></P>
</TD><TD WIDTH=576 VALIGN=TOP><P CLASS='ChapAn'>Effective Date.</P>
</TD></TR>
<TR><TD WIDTH=96 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3Acc9$cid=california$t=document-frame.htm$an=JD_2305$3.0#JD_2305'>Sec. 2305.</A></P>
</TD><TD WIDTH=576 VALIGN=TOP><P CLASS='ChapAn'>Increase of $10 in the Annual Motor Vehicle Registration Fee.</P>
</TD></TR>
<TR><TD WIDTH=96 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3Acc9$cid=california$t=document-frame.htm$an=JD_2306$3.0#JD_2306'>Sec. 2306.</A></P>
</TD><TD WIDTH=576 VALIGN=TOP><P CLASS='ChapAn'>Responsibilities and Powers of the Authority.</P>
</TD></TR>
<TR><TD WIDTH=96 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3Acc9$cid=california$t=document-frame.htm$an=JD_2307$3.0#JD_2307'>Sec. 2307.</A></P>
</TD><TD WIDTH=576 VALIGN=TOP><P CLASS='ChapAn'>Contract with Department of Motor Vehicles.</P>
</TD></TR>
<TR><TD WIDTH=96 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3Acc9$cid=california$t=document-frame.htm$an=JD_2308$3.0#JD_2308'>Sec. 2308.</A></P>
</TD><TD WIDTH=576 VALIGN=TOP><P CLASS='ChapAn'>Use of Proceeds.</P>
</TD></TR>
<TR><TD WIDTH=96 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3Acc9$cid=california$t=document-frame.htm$an=JD_2309$3.0#JD_2309'>Sec. 2309.</A></P>
</TD><TD WIDTH=576 VALIGN=TOP><P CLASS='ChapAn'>Severability.</P>
</TD></TR></TABLE>
<A NAME='JD_2301'></A>
<a name="LPTOC1"></a><H3 CLASS='Section'><a href="javascript:void(0)" onclick="showUrl('JD_2301')"><img src="/alp_templates/images/ui-bookmark.gif" width="16" height="16" alt="Bookmark" border="0"></a><span href="javascript:void(0)" onclick="showUrl('JD_2301')" style="cursor: pointer">SEC. 2301.  TITLE.</span></H3>
<P>     This ordinance shall be known as the "Vehicle Registration Fee Ordinance." </P>
<P CLASS='History'>(Added by Prop. AA, App. 11/2/2010)</P>
<A NAME='JD_2302'></A>
<a name="LPTOC2"></a><H3 CLASS='Section'><a href="javascript:void(0)" onclick="showUrl('JD_2302')"><img src="/alp_templates/images/ui-bookmark.gif" width="16" height="16" alt="Bookmark" border="0"></a><span href="javascript:void(0)" onclick="showUrl('JD_2302')" style="cursor: pointer">SEC. 2302.  DEFINITIONS.</span></H3>
<P>     For the purpose of this Vehicle Registration Fee Ordinance, the following words shall have the meanings set forth below. </P>
<P>     (a)     "Authority." The San Francisco County Transportation Authority.</P>
<P>     (b)     "Board." The Authority Board of Commissioners.</P>
<P>     (c)     "Expenditure Plan." The "SB83 Additional Vehicle Registration Fee Expenditure Plan," approved by the Board on June 29, 2010, to set the transportation projects and programs funded over the next 30 years with the revenues of the fee increase, as well as other allowable costs on which the Authority may spend the proceeds of the $10 vehicle registration fee increase authorized by Section
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3Acc9$cid=california$t=document-frame.htm$an=JD_2305$3.0#JD_2305'>2305</A>. The Expenditure Plan specifies eligibility and other conditions and criteria under which the proceeds of the fee increase are available, and provides for the adoption of future Expenditure Plan updates. </P>
<P CLASS='History'>(Added by Prop. AA, App. 11/2/2010)</P>
<A NAME='JD_2303'></A>
<a name="LPTOC3"></a><H3 CLASS='Section'><a href="javascript:void(0)" onclick="showUrl('JD_2303')"><img src="/alp_templates/images/ui-bookmark.gif" width="16" height="16" alt="Bookmark" border="0"></a><span href="javascript:void(0)" onclick="showUrl('JD_2303')" style="cursor: pointer">SEC. 2303.  PURPOSE.</span></H3>
<P>     The City and County of San Francisco has very significant unfunded transportation needs and this $10 vehicle registration fee increase would provide a stable source of funding to meet some of those needs. The fee is expected to generate approximately $5 million annually that the Authority would use to fund projects and programs under the Expenditure Plan that mitigate congestion and pollution caused by motor vehicles in San Francisco. These projects and programs could include repairing local streets and roads, improving Muni's reliability, pedestrian safety improvements, smart traffic signal technology to prioritize transit and manage traffic incidents, and programs that encourage people to use more sustainable forms of transportation, e.g. transit, bicycle, carpool or on foot. All of the projects and programs must have a relationship or benefit to the persons paying the fee. The Expenditure Plan contains guiding principles intended to, among other objectives, focus on funding smaller, high-impact projects that will quickly provide tangible benefits; provide a fair geographic distribution that takes into account the various needs of San Francisco's neighborhoods; and ensure accountability and transparency in programming and delivery. </P>
<P CLASS='History'>(Added by Prop. AA, App. 11/2/2010)</P>
<A NAME='JD_2304'></A>
<a name="LPTOC4"></a><H3 CLASS='Section'><a href="javascript:void(0)" onclick="showUrl('JD_2304')"><img src="/alp_templates/images/ui-bookmark.gif" width="16" height="16" alt="Bookmark" border="0"></a><span href="javascript:void(0)" onclick="showUrl('JD_2304')" style="cursor: pointer">SEC. 2304.  EFFECTIVE DATE.</span></H3>
<P>     The Vehicle Registration Fee Ordinance shall be effective at the close of the polls in the City and County of San Francisco on the day of the election scheduled for November 2, 2010. </P>
<P CLASS='History'>(Added by Prop. AA, App. 11/2/2010)</P>
<A NAME='JD_2305'></A>
<a name="LPTOC5"></a><H3 CLASS='Section'><a href="javascript:void(0)" onclick="showUrl('JD_2305')"><img src="/alp_templates/images/ui-bookmark.gif" width="16" height="16" alt="Bookmark" border="0"></a><span href="javascript:void(0)" onclick="showUrl('JD_2305')" style="cursor: pointer">SEC. 2305.  INCREASE OF $10 IN THE ANNUAL MOTOR VEHICLE REGISTRATION FEE.</span></H3>
<P>     Beginning six months after the Effective Date, the motor vehicle registration fee for all motor vehicles registered in the City and County of San Francisco is increased by $10 each year, for each original vehicle registration and each vehicle registration renewal. </P>
<P CLASS='History'>(Added by Prop. AA, App. 11/2/2010)</P>
<A NAME='JD_2306'></A>
<a name="LPTOC6"></a><H3 CLASS='Section'><a href="javascript:void(0)" onclick="showUrl('JD_2306')"><img src="/alp_templates/images/ui-bookmark.gif" width="16" height="16" alt="Bookmark" border="0"></a><span href="javascript:void(0)" onclick="showUrl('JD_2306')" style="cursor: pointer">SEC. 2306.  RESPONSIBILITIES AND POWERS OF THE AUTHORITY.</span></H3>
<P>     The Authority shall have all of the powers set forth in California Government Code Section 65089.20, all of the powers set forth in the Expenditure Plan, and all powers incidental or necessary to imposing and collecting the fee increase authorized under Section
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3Acc9$cid=california$t=document-frame.htm$an=JD_2305$3.0#JD_2305'>2305</A>, administering the fee proceeds, the Expenditure Plan, and the projects and programs under that Expenditure Plan, and delivering the transportation improvements in the Expenditure Plan. </P>
<P CLASS='History'>(Added by Prop. AA, App. 11/2/2010)</P>
<A NAME='JD_2307'></A>
<a name="LPTOC7"></a><H3 CLASS='Section'><a href="javascript:void(0)" onclick="showUrl('JD_2307')"><img src="/alp_templates/images/ui-bookmark.gif" width="16" height="16" alt="Bookmark" border="0"></a><span href="javascript:void(0)" onclick="showUrl('JD_2307')" style="cursor: pointer">SEC. 2307.  CONTRACT WITH DEPARTMENT OF MOTOR VEHICLES.</span></H3>
<P>     Consistent with California Vehicle Code Section 9250.4, the Authority shall request and contract with the California Department of Motor Vehicles for the Department of Motor Vehicles to collect and distribute to the Authority the fee imposed under Section
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3Acc9$cid=california$t=document-frame.htm$an=JD_2305$3.0#JD_2305'>2305</A>, upon the original registration or renewal of registration of all motor vehicles registered in the City and County of San Francisco. </P>
<P CLASS='History'>(Added by Prop. AA, App. 11/2/2010)</P>
<A NAME='JD_2308'></A>
<a name="LPTOC8"></a><H3 CLASS='Section'><a href="javascript:void(0)" onclick="showUrl('JD_2308')"><img src="/alp_templates/images/ui-bookmark.gif" width="16" height="16" alt="Bookmark" border="0"></a><span href="javascript:void(0)" onclick="showUrl('JD_2308')" style="cursor: pointer">SEC. 2308.  USE OF PROCEEDS.</span></H3>
<P>     (a)     The Authority shall use the proceeds of the fees under Section
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3Acc9$cid=california$t=document-frame.htm$an=JD_2305$3.0#JD_2305'>2305</A> solely for the projects, programs and purposes set forth in the Expenditure Plan. Pursuant to California Government Code section 65089.20 and as specified in the Expenditure Plan, the Authority shall use not more than five percent of the fee proceeds for administrative costs associated with the programs and projects, including amending the Expenditure Plan. </P>
<P CLASS='History'>(Added by Prop. AA, App. 11/2/2010)</P>
<A NAME='JD_2309'></A>
<a name="LPTOC9"></a><H3 CLASS='Section'><a href="javascript:void(0)" onclick="showUrl('JD_2309')"><img src="/alp_templates/images/ui-bookmark.gif" width="16" height="16" alt="Bookmark" border="0"></a><span href="javascript:void(0)" onclick="showUrl('JD_2309')" style="cursor: pointer">SEC. 2309.  SEVERABILITY.</span></H3>
<P>     If any of the provisions of this ordinance or the application of those provisions to persons or circumstances shall be held invalid, the remainder of those sections or the application of those provisions to persons or circumstances other than those to which it is held invalid shall not be affected thereby. </P>
<P CLASS='History'>(Added by Prop. AA, App. 11/2/2010)</P>


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


html3 = fromstring('''
<div id="ref_id" style="display: none">California/San Francisco Campaign and Governmental Conduct Code/CAMPAIGN AND GOVERNMENTAL CONDUCT CODE </div>
<link rel="stylesheet" type="text/css" href="/nxt/gateway.dll/California/campaign/campaignandgovernmentalconductcode?f=stylesheets$fn=ALP_style.css$3.0" />

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
//		var new_win = window.open("/nxt/gateway.dll/California/campaign/campaignandgovernmentalconductcode?f=templates$fn=document-frameset.htm$3.0", win_name, "resizable=yes,scrollbars=yes,top=0,left=0,width=" + parseInt(screen.availWidth * .75) + ",height=" + parseInt(screen.availHeight *.75));
		var new_win = window.open("/nxt/gateway.dll/California/campaign/campaignandgovernmentalconductcode?f=templates$fn=default.htm$3.0", win_name, "resizable=yes,scrollbars=yes,top=0,left=0,width=" + parseInt(screen.availWidth * .75) + ",height=" + parseInt(screen.availHeight *.75));
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

	<LINK rel="stylesheet" href="/nxt/gateway.dll?f=id$id=campaign.css$t=document-frame.htm$3.0$p=" type="text/css">
<script type="text/javascript" src="/alp_templates/url.js"></script>
</HEAD>
<BODY bgColor=#ffffff>
<form style="margin-bottom:1px;margin-bottom:1px" name="ChangeBox">
<table border="1" width="100%" cellspacing="0" cellpadding="0" style="background-color: #ffffff">
<tr><td>
<p style="margin-bottom:1px;margin-bottom:1px;text-align:center"><span style="font-family:Arial;font-size:8pt"> San Francisco Campaign and Governmental Conduct Code</span></p>
</td></tr>
<tr><td class="refline" bgcolor="#d3d3d3">
<p class="refline" style="margin-left:1px;"><a href="/nxt/gateway.dll?f=id$id=San%20Francisco%20Campaign%20and%20Governmental%20Conduct%20Code%3Ar%3A2$t=document-frame.htm$3.0$p=" class="refline">CAMPAIGN AND GOVERNMENTAL CONDUCT CODE </a></p>
</td></tr>
</table>
</form>
<META http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<A NAME='JD_Campaign'></A>
<H1 CLASS='Article'><a href="javascript:void(0)" onclick="showUrl('')"><img src="/alp_templates/images/ui-bookmark.gif" width="16" height="16" alt="Bookmark" border="0"></a><span href="javascript:void(0)" onclick="showUrl('')" style="cursor: pointer"><B>CAMPAIGN AND GOVERNMENTAL CONDUCT CODE</B> </span></H1>
<P CLASS='Currency'>The San Francisco Municipal Code is current through <A HREF='http://www.sfbos.org/ftp/uploadedfiles/bdsupvrs/ordinances13/o0107-13.pdf' TARGET="_blank">Ordinance 107-13</A>, File No. 130070, approved June 13, 2013, effective July 13, 2013.</P>
<P CLASS='Currency'>The Campaign and Governmental Conduct Code was last amended by <A HREF='http://www.sfbos.org/ftp/uploadedfiles/bdsupvrs/ordinances13/o0009-13.pdf' TARGET="_blank">Ordinance 9-13</A>, File No. 120964, approved February 4, 2013, effective March 6, 2013, operative January 1, 2013.</P>
<P CLASS='Center'><IMG SRC='/nxt/gateway.dll?f=id$id=San%20Francisco%20Campaign%20and%20Governmental%20Conduct%20Code%3Ao%3A27$cid=california$t=document-frame.htm$3.0$p=' BORDER=0 WIDTH=216 HEIGHT=200></P>
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
<P CLASS='Center'><B>AMERICAN LEGAL PUBLISHING CORPORATION<BR />
</B>432 Walnut Street, Suite 1200<BR />
Cincinnati, Ohio  45202-3909<BR />
(800) 445-5588<BR />
Fax: (513) 763-3562<BR />
Email: <A HREF='mailto:customerservice@amlegal.com'>customerservice@amlegal.com</A><BR />
<A HREF='http://www.amlegal.com' TARGET="_blank">www.amlegal.com</A></P>

<a name="LPTOC1"></a><H2 CLASS='Chapter'>PREFACE TO THE <BR />
CAMPAIGN AND GOVERNMENTAL CONDUCT CODE </H2>
<P>     This electronic version of the City and County of San Francisco Municipal Code is updated as amending legislation is approved.  New Ordinance Notices are inserted where applicable to call the user's attention to material that has been affected by legislation that has been passed but is not yet effective.  Any references to such legislation are also compiled in a
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Campaign%20and%20Governmental%20Conduct%20Code%3Ar%3A760$cid=california$t=document-frame.htm$an=JD_NewOrds$3.0#JD_NewOrds'>table</A> at the end of this Code.  The amendments are then incorporated into the Code when they become effective.</P>
<P>     Beginning with ordinances passed in 2011, all ordinances affecting this Code are summarized in a
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Campaign%20and%20Governmental%20Conduct%20Code%3Ar%3A760$cid=california$t=document-frame.htm$an=JD_PRTable$3.0#JD_PRTable'>table</A> that lists the identifying information (ordinance and file numbers), effective date, short title, and sections affected for each such ordinance.  Users should note that the operative date of an ordinance may be later than the effective date of the ordinance.  A delayed operative date will be noted in the ordinance.</P>
<P>     This Code may contain various Editor's Notes (explaining the disposition of or cross referencing various provisions), and/or Codification Notes (documenting scrivener's errors and the like found in the underlying ordinances).  Such notes have been inserted by the publisher for the convenience of the user or as historical references.  They have not been approved or adopted by the City and County of San Francisco, and are of no legal force or effect.</P>

<TABLE CELLSPACING=0 WIDTH=584 CELLPADDING=4>
<TR><TD WIDTH=98 VALIGN=TOP><P CLASS='ChapAn'><B>Article</B></P>
</TD><TD WIDTH=486 VALIGN=TOP> </TD></TR>
<TR><TD WIDTH=98 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Campaign%20and%20Governmental%20Conduct%20Code%3Ar%3Ab$cid=california$t=document-frame.htm$an=JD_ArticleI$3.0#JD_ArticleI'>I. </A></P>
</TD><TD WIDTH=486 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Campaign%20and%20Governmental%20Conduct%20Code%3Ar%3Ab$cid=california$t=document-frame.htm$an=JD_ArticleI$3.0#JD_ArticleI'>ELECTION CAMPAIGNS</A></P>
</TD></TR>
<TR><TD WIDTH=98 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Campaign%20and%20Governmental%20Conduct%20Code%3Ar%3A31e$cid=california$t=document-frame.htm$an=JD_ArticleII$3.0#JD_ArticleII'>II. </A></P>
</TD><TD WIDTH=486 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Campaign%20and%20Governmental%20Conduct%20Code%3Ar%3A31e$cid=california$t=document-frame.htm$an=JD_ArticleII$3.0#JD_ArticleII'>LOBBYING</A></P>
</TD></TR>
<TR><TD WIDTH=98 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Campaign%20and%20Governmental%20Conduct%20Code%3Ar%3A3bb$cid=california$t=document-frame.htm$an=JD_ArticleIII$3.0#JD_ArticleIII'>III. </A></P>
</TD><TD WIDTH=486 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Campaign%20and%20Governmental%20Conduct%20Code%3Ar%3A3bb$cid=california$t=document-frame.htm$an=JD_ArticleIII$3.0#JD_ArticleIII'>CONDUCT OF GOVERNMENT OFFICIALS AND EMPLOYEES</A></P>
</TD></TR>
<TR><TD WIDTH=98 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Campaign%20and%20Governmental%20Conduct%20Code%3Ar%3A705$cid=california$t=document-frame.htm$an=JD_ArticleIV$3.0#JD_ArticleIV'>IV. </A></P>
</TD><TD WIDTH=486 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Campaign%20and%20Governmental%20Conduct%20Code%3Ar%3A705$cid=california$t=document-frame.htm$an=JD_ArticleIV$3.0#JD_ArticleIV'>PROTECTION OF WHISTLEBLOWERS</A></P>
</TD></TR></TABLE>


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


def test_count():
    'The list of articles should have the correct length.'
    expected = 23
    n.assert_equal(len(observed), expected)

def test_data_2():
    number = '2.'
    title = 'LICENSE FEES'
    href = 'http://www.amlegal.com/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A198$cid=california$t=document-frame.htm$an=JD_Article2$3.0#JD_Article2'
    n.assert_tuple_equal(observed[1], (number, title, href))

def test_article23():
    html2.make_links_absolute('http://www.amlegal.com/nxt/gateway.dll\?f\=id\$id\=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3Acc9\$cid\=california\$t\=document-frame.htm\$an\=JD_Article23\$3.0#JD_Article23')
    observed2 = lib.articles(html2)

def test_campaign():
    lib.articles(html3)
