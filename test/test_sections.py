# vim: set fileencoding=utf-8 :
import nose.tools as n
from lxml.html import fromstring

import lib
html = fromstring('''
<div id="ref_id" style="display: none">California/San Francisco Business and Tax Regulations Code/ARTICLE 7: TAX ON TRANSIENT OCCUPANCY OF HOTEL ROOMS</div>
<link rel="stylesheet" type="text/css" href="/nxt/gateway.dll/California/business/article7taxontransientoccupancyofhotelro?f=stylesheets$fn=ALP_style.css$3.0" />

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
//		var new_win = window.open("/nxt/gateway.dll/California/business/article7taxontransientoccupancyofhotelro?f=templates$fn=document-frameset.htm$3.0", win_name, "resizable=yes,scrollbars=yes,top=0,left=0,width=" + parseInt(screen.availWidth * .75) + ",height=" + parseInt(screen.availHeight *.75));
		var new_win = window.open("/nxt/gateway.dll/California/business/article7taxontransientoccupancyofhotelro?f=templates$fn=default.htm$3.0", win_name, "resizable=yes,scrollbars=yes,top=0,left=0,width=" + parseInt(screen.availWidth * .75) + ",height=" + parseInt(screen.availHeight *.75));
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
<p class="refline" style="margin-left:1px;"><a href="/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$t=document-frame.htm$3.0$p=" class="refline">ARTICLE 7: TAX ON TRANSIENT OCCUPANCY OF HOTEL ROOMS</a></p>
</td></tr>
</table>
</form>
<META http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<A NAME='JD_Article7'></A>
<H1 CLASS='Article'><a href="javascript:void(0)" onclick="showUrl('')"><img src="/alp_templates/images/ui-bookmark.gif" width="16" height="16" alt="Bookmark" border="0"></a><span href="javascript:void(0)" onclick="showUrl('')" style="cursor: pointer">ARTICLE 7:<BR />
TAX ON TRANSIENT OCCUPANCY OF HOTEL ROOMS</span></H1>

<TABLE CELLSPACING=0 WIDTH=672 CELLPADDING=4>
<TR><TD WIDTH=120 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_501$3.0#JD_501'>Sec. 501.</A></P>
</TD><TD WIDTH=552 VALIGN=TOP><P CLASS='ChapAn'>Additional Definitions.</P>
</TD></TR>
<TR><TD WIDTH=120 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502$3.0#JD_502'>Sec. 502.</A></P>
</TD><TD WIDTH=552 VALIGN=TOP><P CLASS='ChapAn'>Imposition and Rate of Tax.</P>
</TD></TR>
<TR><TD WIDTH=120 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.5$3.0#JD_502.5'>Sec. 502.5.</A></P>
</TD><TD WIDTH=552 VALIGN=TOP><P CLASS='ChapAn'>Imposition of Surcharge.</P>
</TD></TR>
<TR><TD WIDTH=120 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.6$3.0#JD_502.6'>Sec. 502.6.</A></P>
</TD><TD WIDTH=552 VALIGN=TOP><P CLASS='ChapAn'>Imposition of a 1.25 Percent Surcharge.</P>
</TD></TR>
<TR><TD WIDTH=120 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.6-1$3.0#JD_502.6-1'>Sec. 502.6-1.</A></P>
</TD><TD WIDTH=552 VALIGN=TOP><P CLASS='ChapAn'>Imposition of a Cumulative Surcharge.</P>
</TD></TR>
<TR><TD WIDTH=120 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.6-2$3.0#JD_502.6-2'>Sec. 502.6-2.</A></P>
</TD><TD WIDTH=552 VALIGN=TOP><P CLASS='ChapAn'>Continuation of Two Percent Hotel Tax Surcharge.</P>
</TD></TR>
<TR><TD WIDTH=120 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.7$3.0#JD_502.7'>Sec. 502.7.</A></P>
</TD><TD WIDTH=552 VALIGN=TOP><P CLASS='ChapAn'>Temporary Suspension of Tax and Surcharges for Occupancies in Hotels in Certain Redevelopment Project Areas.</P>
</TD></TR>
<TR><TD WIDTH=120 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.8$3.0#JD_502.8'>Sec. 502.8.</A></P>
</TD><TD WIDTH=552 VALIGN=TOP><P CLASS='ChapAn'>Imposition and Rate of Tax in Certain Redevelopment Project Areas  Transient Occupancy Tax  San Francisco Redevelopment Agency.</P>
</TD></TR>
<TR><TD WIDTH=120 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.8-1$3.0#JD_502.8-1'>Sec. 502.8-1.</A></P>
</TD><TD WIDTH=552 VALIGN=TOP><P CLASS='ChapAn'>Imposition of Additional Surcharge in Certain Redevelopment Project Areas.</P>
</TD></TR>
<TR><TD WIDTH=120 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_503$3.0#JD_503'>Sec. 503.</A></P>
</TD><TD WIDTH=552 VALIGN=TOP><P CLASS='ChapAn'>Occupant to Pay Tax to Operator.</P>
</TD></TR>
<TR><TD WIDTH=120 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_504$3.0#JD_504'>Sec. 504.</A></P>
</TD><TD WIDTH=552 VALIGN=TOP><P CLASS='ChapAn'>Collection of Tax by Operator; Receipt to Occupant; Rules for Collection Schedules.</P>
</TD></TR>
<TR><TD WIDTH=120 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_505$3.0#JD_505'>Sec. 505.</A></P>
</TD><TD WIDTH=552 VALIGN=TOP><P CLASS='ChapAn'>Unlawful Advertising Regarding Tax.</P>
</TD></TR>
<TR><TD WIDTH=120 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_506$3.0#JD_506'>Sec. 506.</A></P>
</TD><TD WIDTH=552 VALIGN=TOP><P CLASS='ChapAn'>Additional Exemptions.</P>
</TD></TR>
<TR><TD WIDTH=120 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_515.01$3.0#JD_515.01'>Sec. 515.01.</A></P>
</TD><TD WIDTH=552 VALIGN=TOP><P CLASS='ChapAn'>Hotel Tax Allocations.</P>
</TD></TR>
<TR><TD WIDTH=120 VALIGN=TOP><P CLASS='ChapAn'>
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_515.2$3.0#JD_515.2'>Sec. 515.2.</A></P>
</TD><TD WIDTH=552 VALIGN=TOP><P CLASS='ChapAn'>Calculation of Percentage Allocations under Section 515.</P>
</TD></TR></TABLE>
<A NAME='JD_501'></A>
<a name="LPTOC1"></a><H3 CLASS='Section'><a href="javascript:void(0)" onclick="showUrl('JD_501')"><img src="/alp_templates/images/ui-bookmark.gif" width="16" height="16" alt="Bookmark" border="0"></a><span href="javascript:void(0)" onclick="showUrl('JD_501')" style="cursor: pointer">SEC. 501.  ADDITIONAL DEFINITIONS.</span></H3>
<P>     When used in this Article the following terms shall mean or include: </P>
<P>     (a)     "Operator." Any person operating a hotel in the City and County of San Francisco, including, but not limited to, the owner or proprietor of such premises, lessee, sublessee, mortgagee in possession, licensee or any other person otherwise operating such hotel. </P>
<P>     (b)     "Occupant." A person who, for a consideration, uses, possesses, or has the right to use or possess any room in a hotel under any lease, concession, permit, right of access, license to use or other agreement, or otherwise. </P>
<P>     (c)     "Occupancy." The use or possession, or the right to the use or possession of any room or apartment in a hotel or the right to the use or possession of the furnishings or to the services and accommodations accompanying the use and possession of the room. </P>
<P>     (d)     "Hotel." Any structure, or any portion of a structure, including any lodginghouse, roominghouse, dormitory, Turkish bath, bachelor hotel, studio hotel, motel, auto court, inn, public club, or private club, containing guest rooms and which is occupied, or is intended or designated for occupation, by guests, whether rent is paid in money, goods, labor, or otherwise. It does not include any jail, hospital, asylum, sanitarium, orphanage, prison, detention, or other building in which human beings are housed and detained under legal restraint. </P>
<P>     (e)     "Guest Room." A room occupied, or intended, arranged, or designed for occupation, by one or more occupants. Every 100 square feet of superficial floor area in a dormitory is a guest room. </P>
<P>     (f)     "Rent." The consideration received for occupancy valued in money, whether received in money or otherwise, including all receipts, cash, credits, and property or services of any kind or nature, and also the amount for which credit is allowed by the operator to the occupant, without any deduction therefrom whatsoever. </P>
<P>     (g)     "Permanent Resident." Any occupant as of a given date who has or shall have occupied, or has or shall have the right of occupancy, of any guest room in a hotel for at least 30 consecutive days next preceding such date. </P>
<P CLASS='History'>(Added by Ord. 87-61, App. 4/26/61; amended by Ord. 231-91, App. 6/12/91; Ord. 19-98, App. 1/16/98)</P>
<A NAME='JD_502'></A>
<a name="LPTOC2"></a><H3 CLASS='Section'><a href="javascript:void(0)" onclick="showUrl('JD_502')"><img src="/alp_templates/images/ui-bookmark.gif" width="16" height="16" alt="Bookmark" border="0"></a><span href="javascript:void(0)" onclick="showUrl('JD_502')" style="cursor: pointer">SEC. 502.  IMPOSITION AND RATE OF TAX.</span></H3>
<P>     There shall be paid a tax of eight percentum on the rent for every occupancy of a guest room in a hotel in the City and County. </P>
<P CLASS='History'>(Amended by Ord. 251-78, App. 6/1/78; Ord. 19-98, App. 1/16/98)</P>
<A NAME='JD_502.5'></A>
<a name="LPTOC3"></a><H3 CLASS='Section'><a href="javascript:void(0)" onclick="showUrl('JD_502.5')"><img src="/alp_templates/images/ui-bookmark.gif" width="16" height="16" alt="Bookmark" border="0"></a><span href="javascript:void(0)" onclick="showUrl('JD_502.5')" style="cursor: pointer">SEC. 502.5.  IMPOSITION OF SURCHARGE.</span></H3>
<P>     There shall be an additional tax of 1.75 percent on the rent for every occupancy of the guest rooms in a hotel in the City and County of San Francisco between July 1, 1980 and August 14, 1993 and an additional tax of 2.75 percent on the rent for every occupancy on and after August 15, 1993. </P>
<P>     When rent is paid, charged, billed or falls due on either a weekly, monthly or other term basis, the rent so paid, charged, billed or falling due shall be subject to the tax of eight percent herein imposed to the extent that it covers any portion of the period prior to July 1, 1980, and to the tax of eight percent herein plus the 1.75 percent surcharge imposed to the extent that it covers any portion of the period between July 1, 1980 and August 14, 1993, and the 2.75 percent surcharge imposed to the extent that it covers any portion of the period on and after August 15, 1993, and such payment, charge, bill or rent due shall be apportioned on the basis of the ratio of the number of days falling within the periods prior to July 1, 1980, between July 1, 1980 and August 14, 1993, and on and after August 15, 1993 to the total number of days covered thereby. Where any tax has been paid hereunder upon any rent without any right of occupancy therefor, the Tax Collector may by regulation provide for credit or refund of the amount of such tax upon application therefor as provided in this Code. </P>
<P>     The surcharge tax so collected shall be deposited in the General Fund subject to appropriation pursuant to the budget and fiscal provisions of the Charter. </P>
<P>     By adopting this ordinance the People of the City and County of San Francisco do not intend to limit or in anyway curtail any powers the Board of Supervisors may exercise as to the subject matter of this ordinance, including, but not limited to, raising the rate of taxation or surcharge, lowering the rate of taxation or surcharge, eliminating the tax or surcharge, or creating or defining new categories of taxpayers under this ordinance. </P>
<P CLASS='History'>(Added by 6/3/80; portions of this Section require ballot measure to amend; amended by Ord. 244-93, App. 8/10/93; Ord. 19-98, App. 1/16/98) </P>
<A NAME='JD_502.6'></A>
<a name="LPTOC4"></a><H3 CLASS='Section'><a href="javascript:void(0)" onclick="showUrl('JD_502.6')"><img src="/alp_templates/images/ui-bookmark.gif" width="16" height="16" alt="Bookmark" border="0"></a><span href="javascript:void(0)" onclick="showUrl('JD_502.6')" style="cursor: pointer">SEC. 502.6.  IMPOSITION OF A 1.25 PERCENT SURCHARGE.</span></H3>
<P>     (a)     There shall be an additional tax of 1.25 percent on the rent for every occupancy of the guest rooms in the hotel in the City and County of San Francisco on and after January 1, 1987. </P>
<P>     (b)     When rent is paid, charged, billed or falls due on either weekly, monthly or other term basis, the rent so paid, charged, billed or falling due shall be subject to the tax of 9.75 percentum herein imposed to the extent that it covers any portion of the period prior to January 1, 1987, and to the tax of 9.75 percent herein plus the amount of surcharge imposed to the extent that it covers any portion of the period on and after January 1, 1987 and such payment, charge, bill or rent due shall be apportioned on the basis of the ratio of the number of days falling within said periods to the total number of days covered thereby. Where any tax has been paid hereunder upon any rent without any right of occupancy therefor the Tax Collector may by regulation provide for credit or refund of the amount of such tax upon application therefor as provided in this Code. </P>
<P>     (c)     The surcharge tax so collected shall be deposited in the General Fund subject to appropriation pursuant to the budget and fiscal provisions of the Charter. </P>
<P CLASS='History'>(Added by Ord. 468-86, App. 12/5/86; amended by Ord. 19-98, App. 1/16/98)</P>
<A NAME='JD_502.6-1'></A>
<a name="LPTOC5"></a><H3 CLASS='Section'><a href="javascript:void(0)" onclick="showUrl('JD_502.6-1')"><img src="/alp_templates/images/ui-bookmark.gif" width="16" height="16" alt="Bookmark" border="0"></a><span href="javascript:void(0)" onclick="showUrl('JD_502.6-1')" style="cursor: pointer">SEC. 502.6-1.  IMPOSITION OF A CUMULATIVE SURCHARGE.</span></H3>
<P>     (a)     <B>Replacement of Section
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.5$3.0#JD_502.5'>502.5</A> and Section
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.6$3.0#JD_502.6'>502.6</A>.</B> Commencing on August 1, 1996, Section
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.5$3.0#JD_502.5'>502.5</A> and Section
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.6$3.0#JD_502.6'>502.6</A> are hereby suspended and replaced in their entirety by this new Section
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.6-1$3.0#JD_502.6-1'>502.6-1</A>. The purpose of this new Section is to combine the surcharges levied by Sections
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.5$3.0#JD_502.5'>502.5</A> and
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.6$3.0#JD_502.6'>502.6</A> and to increase the total surcharge levied by the City and County by two percent. In the event any portion of the transient occupancy tax levied by the City pursuant to Section
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.6-1$3.0#JD_502.6-1'>502.6-1</A> hereof is found to be invalid, illegal or unconstitutional, the suspension of Sections
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.5$3.0#JD_502.5'>502.5</A> and
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.6$3.0#JD_502.6'>502.6</A> shall be rescinded by operation of law and the taxes and surcharges levied under such Sections shall be deemed to have been in full force and effect during the period the City collected the taxes under the authority of this Section. </P>
<P>     (b)     <B>Imposition of Surcharge.</B> Effective August 1, 1996, there shall be a surcharge of six percent, in addition to the eight percent tax specified in Section
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502$3.0#JD_502'>502</A>, on the rent for every occupancy of the guest room in a hotel in the City and County of San Francisco. The surcharge so collected shall be deposited in the General Fund subject to appropriation pursuant to the budget and fiscal provisions of the Charter. </P>
<P>     (c)     <B>Prorata Allocation of Surcharge.</B> When rent is paid, charged, billed or falls due on either a weekly, monthly or other term basis, the rent so paid, charged, billed or falling due shall be subject to a surcharge of four percent to the extent that it covers any portion of the period prior to August 1, 1996, and a six percent surcharge to the extent that it covers any portion of the period on or after August 1, 1996, and such payment, charge, bill or rent due shall be apportioned on the basis of the ratio of the number of days falling within said periods to the total number of days covered by such payment. Where any surcharge has been paid hereunder upon any rent without any right of occupancy therefor, the Tax Collector may by regulation provide for credit or refund of the amount of such tax upon application therefor as provided in this Code. </P>
<P>     (d)     <B>Suspension of Surcharge Pursuant to Section
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.7$3.0#JD_502.7'>502.7</A>.</B> The provisions of this Section
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.6-1$3.0#JD_502.6-1'>502.6-1</A> shall be subject to Section
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.7$3.0#JD_502.7'>502.7</A>, including the temporary suspension provided therein. </P>
<P CLASS='History'>(Added by Ord. 290-96, App. 7/12/96; amended by Ord. 19-98, App. 1/16/98)</P>
<A NAME='JD_502.6-2'></A>
<a name="LPTOC6"></a><H3 CLASS='Section'><a href="javascript:void(0)" onclick="showUrl('JD_502.6-2')"><img src="/alp_templates/images/ui-bookmark.gif" width="16" height="16" alt="Bookmark" border="0"></a><span href="javascript:void(0)" onclick="showUrl('JD_502.6-2')" style="cursor: pointer">SEC. 502.6-2.  CONTINUATION OF TWO PERCENT HOTEL TAX SURCHARGE.</span></H3>
<P>     The City and County of San Francisco is hereby authorized to continue to levy and collect a two percent hotel tax surcharge imposed by Section
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.6-1$3.0#JD_502.6-1'>502.6-1</A>. All monies derived from the collection of such two percent hotel tax surcharge shall be deposited in the General Fund of the City and County of San Francisco and, subject to the budgetary and fiscal provisions of the Charter, may be expended for any lawful City and County of San Francisco purposes. </P>
<P CLASS='History'>(Added by Proposition H, 11/3/98)</P>
<A NAME='JD_502.7'></A>
<a name="LPTOC7"></a><H3 CLASS='Section'><a href="javascript:void(0)" onclick="showUrl('JD_502.7')"><img src="/alp_templates/images/ui-bookmark.gif" width="16" height="16" alt="Bookmark" border="0"></a><span href="javascript:void(0)" onclick="showUrl('JD_502.7')" style="cursor: pointer">SEC. 502.7.  TEMPORARY SUSPENSION OF TAX AND SURCHARGES FOR OCCUPANCIES IN HOTELS IN CERTAIN REDEVELOPMENT PROJECT AREAS.</span></H3>
<P>     (a)     <B>Suspension.</B> Commencing on October 1, 1994, the provisions of Sections
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502$3.0#JD_502'>502</A>,
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.5$3.0#JD_502.5'>502.5</A> and
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.6$3.0#JD_502.6'>502.6</A> hereof shall be temporarily suspended and inapplicable to the occupancy of any guest room in any hotel located within the boundaries of the following San Francisco Redevelopment Agency Project Areas: </P>
<P>          (1)     Yerba Buena Center Project Area, as described in the Redevelopment Plan adopted by the Board of Supervisors on April 25, 1966, as amended on July 26, 1971, October 9, 1973, September 13, 1976, August 8, 1977, August 13, 1979, November 2, 1981 and December 1, 1986; </P>
<P>          (2)     Embarcadero-Lower Market (Golden Gateway) Project Area, as described in the Redevelopment Plan adopted by the Board of Supervisors on May 25, 1959, as amended on July 31, 1961, July 13, 1964, November 23, 1964, May 15, 1967, July 22, 1968, November 29, 1976 and December 1, 1986; </P>
<P>          (3)     Western Addition Project Area A-1, as described in the Redevelopment Plan adopted by the Board of Supervisors on May 28, 1956, as amended on January 30, 1961, July 31, 1961, January 14, 1963, February 25, 1963, July 3, 1964, October 26, 1981 and May 3, 1985; </P>
<P>          (4)     Western Addition Project Area A-2, as described in the Redevelopment Plan adopted by the Board of Supervisors on October 13, 1964, as amended on August 3, 1970, June 6, 1976, December 15, 1986, November 9, 1987 and August 10, 1992; </P>
<P>          (5)     South of Market Earthquake Recovery Redevelopment Plan (South of Market Project Area), as described in the Redevelopment Plan adopted by the Board of Supervisors on June 11, 1990; and </P>
<P>          (6)     Chinese Cultural and Trade Center Redevelopment Project Area, as described in the Redevelopment Plan adopted by the Board of Supervisors on November 8, 1965. </P>
<P>          Each of the foregoing project areas shall hereinafter be individually referred to as a "SFRA Project Area." </P>
<P>     (b)     <B>Duration.</B> The foregoing suspension of Sections
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502$3.0#JD_502'>502</A>,
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.5$3.0#JD_502.5'>502.5</A> and
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.6$3.0#JD_502.6'>502.6</A> shall continue and remain in effect so long as Section
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.8$3.0#JD_502.8'>502.8</A> remains in effect. Immediately upon Section
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.8$3.0#JD_502.8'>502.8</A> no longer being effective, Sections
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502$3.0#JD_502'>502</A>,
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.5$3.0#JD_502.5'>502.5</A> and
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.6$3.0#JD_502.6'>502.6</A> shall again apply to all the SFRA Project Areas. In the event any portion of the transient occupancy tax levied by the City pursuant to Section
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.8$3.0#JD_502.8'>502.8</A> hereof is found to be invalid, illegal or unconstitutional, the suspension of Sections
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502$3.0#JD_502'>502</A>,
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.5$3.0#JD_502.5'>502.5</A> and
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.6$3.0#JD_502.6'>502.6</A> shall be rescinded by operation of law and the taxes and surcharges levied under such Sections shall be deemed to have been in full force and effect during the period the City collected the transient occupancy tax found to be invalid, illegal or unconstitutional. </P>
<P CLASS='History'>(Added by Ord. 246-94, App. 6/30/94)</P>
<A NAME='JD_502.8'></A>
<a name="LPTOC8"></a><H3 CLASS='Section'><a href="javascript:void(0)" onclick="showUrl('JD_502.8')"><img src="/alp_templates/images/ui-bookmark.gif" width="16" height="16" alt="Bookmark" border="0"></a><span href="javascript:void(0)" onclick="showUrl('JD_502.8')" style="cursor: pointer">SEC. 502.8.  IMPOSITION AND RATE OF TAX IN CERTAIN REDEVELOPMENT PROJECT AREAS  TRANSIENT OCCUPANCY TAX  SAN FRANCISCO REDEVELOPMENT AGENCY.</span></H3>
<P>     (a)     <B>Imposition and Rate of Tax.</B> Pursuant to Section 7280 of the California Revenue and Taxation Code, the City hereby imposes a tax of 12 percent on the rent for every occupancy of a guest room in any hotel located within the boundaries of a SFRA Project Area. The foregoing tax shall be effective on October 1, 1994. The tax so collected shall be deposited in the General Fund subject to appropriation pursuant to the budget and fiscal provisions of the Charter. The tax shall be subject to all the provisions of this Article and shall be administered accordingly by the Tax Collector. </P>
<P>     (b)     <B>Apportionment of Tax.</B> When rent is paid, charged, billed or falls due on either a weekly, monthly or other term basis, the rent so paid, charged, billed or falling due shall be subject to the tax of 12 percent herein imposed to the extent that it covers any portion of the period after October 1, 1994, and such payment, charge, bill or amount due shall be apportioned on the basis of the ratio of the number of days falling after October 1, 1994, to the total number of days covered thereby. Where any tax has been paid hereunder upon any rent without any right of occupancy therefor the Tax Collector may by regulation provide for credit or refund of the amount of such tax upon application therefor as provided in this Code. </P>
<P>     (c)     <B>Credit for Taxes Paid to San Francisco Redevelopment Agency.</B> In the event a transient occupancy tax is levied by the San Francisco Redevelopment Agency on the rent for the occupancy of a guest room in a hotel located within a SFRA Project Area, a credit in the amount set forth in Subsection (d) below shall be applied against the amounts otherwise due and payable to the City under Section
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.8$3.0#JD_502.8'>502.8</A>(a). The foregoing credit is only applicable to a transient occupancy tax levied by the San Francisco Redevelopment Agency pursuant to the California Revenue and Taxation Code Section 7280.5 for the purpose of paying debt service (as defined below) on bonded indebtedness issued by the San Francisco Redevelopment Agency (the "agency bonds") for redevelopment purposes. </P>
<P>     (d)     <B>Amount of Credit.</B> The aggregate amount of the credit for each fiscal year shall not exceed the debt service on the agency bonds due and payable for that fiscal year. "Debt service" means (i) all payments of principal of and interest on the agency bonds, (ii) any required payment made by the Agency to a bond reserve account established under the agency bond indenture for the exclusive benefit of the agency bonds and (iii) any fee charged by the Tax Collector or the Controller pursuant to Subsection (e) below. </P>
<P>     (e)     <B>Administration of Agency Tax.</B> The Tax Collector and the Controller are hereby authorized to enter into a tax administration agreement with the San Francisco Redevelopment Agency to administer any transient occupancy tax levied by the San Francisco Redevelopment Agency, including collection of taxes and assessment of penalties and interest and any other tax collection functions associated with such levy. Monies collected on behalf of the San Francisco Redevelopment Agency shall be transmitted to the San Francisco Redevelopment Agency for use in accordance with the requirements of the agency bonds and the tax administration agreement. The Tax Collector and the Controller may charge the San Francisco Redevelopment Agency a reasonable fee to compensate for its actual costs of collection and administration services. </P>
<P>     (f)     <B>Limitations on Effectiveness.</B> Section
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.8$3.0#JD_502.8'>502.8</A> shall be of no further force or effect on December 31, 2027 or, in the event of a default on the agency bonds, on the date that such bonds are discharged. </P>
<P CLASS='History'>(Added by Ord. 227-94, App. 6/9/94; amended by Ord. 19-98, App. 1/16/98)</P>
<A NAME='JD_502.8-1'></A>
<a name="LPTOC9"></a><H3 CLASS='Section'><a href="javascript:void(0)" onclick="showUrl('JD_502.8-1')"><img src="/alp_templates/images/ui-bookmark.gif" width="16" height="16" alt="Bookmark" border="0"></a><span href="javascript:void(0)" onclick="showUrl('JD_502.8-1')" style="cursor: pointer">SEC. 502.8-1.  IMPOSITION OF ADDITIONAL SURCHARGE IN CERTAIN REDEVELOPMENT PROJECT AREAS.</span></H3>
<P>     (a)     <B>Imposition of Surcharge.</B> Effective August 1, 1996, there shall be a surcharge of two percent, in addition to the 12 percent tax specified in Section
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.8$3.0#JD_502.8'>502.8</A>, on the rent for every occupancy of the guest rooms in a hotel located within the boundaries of a SFRA Project Area (as such area is defined in Section
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.7$3.0#JD_502.7'>502.7</A>). The surcharge so collected shall be deposited in the General Fund subject to appropriation pursuant to the budget and fiscal provisions of the Charter. </P>
<P>     (b)     <B>Prorata Allocation of Tax and Surcharge.</B> When rent is paid, charged, billed or falls due on either a weekly, monthly or other term basis, the rent so paid, charged, billed or falling due shall be subject to a tax of 12 percent to the extent that it covers any portion of the period prior to August 1, 1996, and to the tax of 12 percent plus the two percent surcharge herein imposed to the extent that it covers any portion of the period on or after August 1, 1996, and such payment, charge, bill or rent due shall be apportioned on the basis of the ratio of the number of days falling within said periods to the total number of days covered by such payment. Where any surcharge has been paid hereunder upon any rent without any right of occupancy therefor, the Tax Collector may by regulation provide for credit or refund of the amount of such tax upon application therefor as provided in this Code. </P>
<P>     (c)     <B>No Credit for Transient Occupancy Taxes Paid to the San Francisco Redevelopment Agency.</B> The credit in Section
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.8$3.0#JD_502.8'>502.8</A>(c) for a transient occupancy tax levied by and paid to the San Francisco Redevelopment Agency shall not be applicable to the surcharge levied pursuant to this Section. </P>
<P>     (d)     <B>Limitations of Effectiveness.</B> Section
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.8-1$3.0#JD_502.8-1'>502.8-1</A> shall be of no further force or effect on and after December 31, 2027 or, in the event of a default on the agency bonds (as defined in Section 502.8 above), on the date that such bonds are discharged. </P>
<P CLASS='History'>(Added by Ord. 290-96, App. 7/12/96; amended by Ord. 19-98, App. 1/16/98)</P>
<A NAME='JD_503'></A>
<a name="LPTOC10"></a><H3 CLASS='Section'><a href="javascript:void(0)" onclick="showUrl('JD_503')"><img src="/alp_templates/images/ui-bookmark.gif" width="16" height="16" alt="Bookmark" border="0"></a><span href="javascript:void(0)" onclick="showUrl('JD_503')" style="cursor: pointer">SEC. 503.  OCCUPANT TO PAY TAX TO OPERATOR.</span></H3>
<P>     Unless prohibited by the laws of the United States or the State of California, or exempted by the provisions of this Article, every occupant occupying a guest room in a hotel in this City and County shall be required to pay the tax imposed herein to the operator along with the rent for the occupancy. This obligation is not satisfied until the tax has been paid to this City and County, except that a receipt indicating payment of the rent from an operator maintaining a place of business in this City and County or from an operator who is authorized by the Tax Collector to collect the tax shall be sufficient to relieve the occupant from further liability for the tax to which the receipt refers. </P>
<P CLASS='History'>(Amended by Ord. 395-84, App. 9/20/84)</P>
<A NAME='JD_504'></A>
<a name="LPTOC11"></a><H3 CLASS='Section'><a href="javascript:void(0)" onclick="showUrl('JD_504')"><img src="/alp_templates/images/ui-bookmark.gif" width="16" height="16" alt="Bookmark" border="0"></a><span href="javascript:void(0)" onclick="showUrl('JD_504')" style="cursor: pointer">SEC. 504.  COLLECTION OF TAX BY OPERATOR; RECEIPT TO OCCUPANT; RULES FOR COLLECTION SCHEDULES.</span></H3>
<P>     Every operator maintaining a place of business in this City and County as provided in Section
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_503$3.0#JD_503'>503</A> herein, and renting guest rooms in this City and County to an occupant, not exempted under Section
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_506$3.0#JD_506'>506</A> of this Article shall, at the time of collecting the rent from the occupant, also collect the tax from the occupant and on demand shall give to the occupant a receipt therefor. In all cases in which the tax is not collected by the operator, as aforesaid, the operator shall be liable to the Tax Collector of the City and County for the amount of the tax due on the amount of taxable rent collected from the occupant under the provisions of this Article, the same as though the tax were paid by the occupant. In all cases of transactions upon credit or deferred payment, the payment of tax to the Tax Collector may be deferred in accordance therewith, and the operator shall be liable therefor at the time and to the extent that such credits are paid or deferred payments are made in accordance with the rate of tax owing on the amount thereof. </P>
<P>     The Tax Collector shall have the power to adopt rules and regulations prescribing methods and schedules for the collection and payment of the tax and such methods and schedules shall eliminate fractions of one cent. </P>
<P CLASS='History'>(Amended by Ord. 395-84, App. 9/20/84)</P>
<A NAME='JD_505'></A>
<a name="LPTOC12"></a><H3 CLASS='Section'><a href="javascript:void(0)" onclick="showUrl('JD_505')"><img src="/alp_templates/images/ui-bookmark.gif" width="16" height="16" alt="Bookmark" border="0"></a><span href="javascript:void(0)" onclick="showUrl('JD_505')" style="cursor: pointer">SEC. 505.  UNLAWFUL ADVERTISING REGARDING TAX.</span></H3>
<P>     It is unlawful for any operator to advertise or hold out or state to the public or to any guest, directly or indirectly, that the tax or any part thereof will be assumed or absorbed by the operator or that it will not be added to the rental of the guest room, or that, if added, it or any part thereof will be refunded. </P>
<P CLASS='History'>(Added by Ord. 87-61, App. 4/26/61)</P>
<A NAME='JD_506'></A>
<a name="LPTOC13"></a><H3 CLASS='Section'><a href="javascript:void(0)" onclick="showUrl('JD_506')"><img src="/alp_templates/images/ui-bookmark.gif" width="16" height="16" alt="Bookmark" border="0"></a><span href="javascript:void(0)" onclick="showUrl('JD_506')" style="cursor: pointer">SEC. 506.  ADDITIONAL EXEMPTIONS.</span></H3>
<P>     No tax shall be imposed hereunder: </P>
<P>     (a)     Upon a permanent resident;</P>
<P>     (b)     Upon a corporation or association having a formally recognized exemption from income taxation pursuant to Section 501(c) or 501(d) or 401(a) of Title 26 of the United States Code as qualified by Sections 502, 503, 504 and 508 of Title 26 of the United States Code; </P>
<P>     (c)     Where the rent is less than at the rate of $30 a day or $100 per week. For multiple-occupancy guest rooms where the hotel determines who will share the rooms, the exemption shall be based on the rent charged per person. </P>
<P CLASS='History'>(Amended by Ord. 395-84, App. 9/20/84; Ord. 368-86  1, App. 8/29/86; Ord. 19-98, App. 1/16/98; Ord. 113-98, App. 4/2/98; Ord. 291-00, File No. 001676, App. 12/22/2000) </P>
<A NAME='JD_515.01'></A>
<a name="LPTOC14"></a><H3 CLASS='Section'><a href="javascript:void(0)" onclick="showUrl('JD_515.01')"><img src="/alp_templates/images/ui-bookmark.gif" width="16" height="16" alt="Bookmark" border="0"></a><span href="javascript:void(0)" onclick="showUrl('JD_515.01')" style="cursor: pointer">SEC. 515.01.  HOTEL TAX ALLOCATIONS.</span></H3>
<P>     (a)     All monies collected pursuant to the tax imposed by Section
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502$3.0#JD_502'>502</A> of this Article ("Hotel Tax Revenues") shall be allocated for the purposes specified in Subsection (b) in the amounts prescribed in Subsection (c), subject to the adjustments and limitations prescribed in Subsection (d). Any unexpended balances remaining in Allocations Number 1, 2, 3, 4, 5, 9 and 10 at the close of any fiscal year shall be deemed to be provided for a specific purpose within the meaning of Section
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Charter%3Ar%3A370$cid=california$t=document-frame.htm$an=JD_9.113$3.0#JD_9.113'>9.113</A> of the Charter and shall be carried forward and accumulated in said allocations for the purposes prescribed in Subsection (b). After the specific purpose allocations and accumulations required by this Section, all remaining revenues shall be transferred to the General Fund, of which an amount not to exceed two tenths of one percent (0.2%) shall be appropriated to the Tax Collector for the administration of the provisions of this Article. </P>
<P>     (b)     The monies allocated pursuant to this Section shall be appropriated to the following departments and used solely for the following purposes: </P>
<P>          (1)     Allocation Number 1 (Convention Facilities): To the City Administrator for Base Rental and Additional Rental as provided for and defined in the Project Lease, as amended, between the City and the San Francisco Redevelopment Agency, for the acquisition, construction and financing of a convention center within the Yerba Buena Center Redevelopment Project Area, and for all expenses reasonably related to operation, maintenance and improvement of the Moscone Convention Center, Brooks Hall and Civic Auditorium. </P>
<P>          (2)     Allocation Number 2 (Convention and Visitors Bureau): To the City Administrator to contract with the San Francisco Convention and Visitors Bureau, pursuant to the authority granted by Section
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Charter%3Ar%3A66$cid=california$t=document-frame.htm$an=JD_3.104$3.0#JD_3.104'>3.104</A> of the San Francisco Charter, to pay administrative and operating expenses of the Convention and Visitors Bureau. </P>
<P>          (3)     Allocation Number 3 (Low-Income Housing in the Yerba Buena Center Redevelopment Project Area): To the Mayor to facilitate the construction of low-income housing in the Project Area and on certain parcels adjacent thereto, including, as may be necessary, payments for architecture, engineering, maintenance and operation, construction, financing and rent supplements for low-income households. Expenditures from Allocation Number 3 shall be made according to the following priorities: </P>
<P>               (A)     The Mayor shall allocate and set aside Hotel Tax Revenues from Allocation Number 3 the amount required for transfer to the rent supplement program established by
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Administrative%20Code%3Ar%3A388e$cid=california$t=document-frame.htm$an=JD_Chapter24A$3.0#JD_Chapter24A'>Chapter 24A</A> of the Administrative Code under the jurisdiction of the Mayor for rent supplements for low-income households and administration costs not to exceed eight percent (8%) of the total sum allocated for rent supplements. </P>
<P>               (B)     The funds next available in excess of the amount required for the purposes described in (A) above shall be used exclusively to facilitate development of low-cost housing in the Project Area and on certain parcels adjacent thereto, including, but not limited to, expenses pertaining to the preparation of architectural and engineering programs, plans, specifications, estimates, land acquisition and expenses incurred by the City. </P>
<P>               (C)     The funds next available in excess of the amount required for the purposes described in (A) and (B) above shall be used exclusively to finance the construction of low-cost housing in the Project Area and on certain parcels adjacent thereto, including lease rental payment in support of Redevelopment Agency bonds in the maximum principal amount feasible pursuant to the Controller's estimate of future monies to be allocated pursuant to Allocation Number 3, or, alternatively, mortgage payments for other financing used to facilitate the construction of housing; and also including costs of maintenance, operation, furniture and equipment relative to said housing and the administration thereof. </P>
<P>               (D)     The funds next available in excess of the amount required for the purposes described in (A), (B) and (C) above shall be used to provide the funds necessary to reduce rentals to 100 percent of the units of housing constructed in the Project Area and on certain parcels adjacent thereto to rent-level categories equivalent to those then in effect in public housing in the City. </P>
<P>               (E)     The funds next available in excess of the amount required for the purposes described in (A), (B), (C) and (D) above shall be retained in a maintenance, operation, furniture and equipment reserve fund to insure the maintenance and operation of the housing constructed in the Project Area and on certain parcels adjacent thereto. </P>
<P>               (F)     Funds next available in excess of the amount required for the purposes described in (A), (B), (C), (D) and (E) above shall be applied to construct or rehabilitate low-income rental housing for the elderly and handicapped in San Francisco which meet all of the following criteria: </P>
<P>                    (i)     One hundred percent of the units are rental, excepting staff-occupied units, which are affordable to low-income elderly or handicapped residents and will remain so for 40 years; </P>
<P>                    (ii)     The project is developed and controlled during that period by a nonprofit corporation, not excluding partnership ownership where the nonprofit corporation is the managing general partner; </P>
<P>                    (iii)     Additional project funding includes funding from sources other than City and County of San Francisco.</P>
<P>               (G)     The funds next available in excess of the amount required for the purposes described in (A), (B), (C), (D), (E) and (F) above may be applied, at the sole option of the City, to the early retirement of bonds or other evidence of indebtedness used to finance low-cost housing in the Project Area or certain parcels adjacent thereto; or may be applied to pay for bridges, ramps, concourse and landscaping to further enhance the convention center in the Project Area. </P>
<P>               (H)     Notwithstanding any other provisions of Allocation 3, to the extent that the City becomes obligated to make lease rental payments to the Redevelopment Agency in support of Redevelopment Agency low-income housing lease revenue bonds or a series of such bonds, the obligation of the City to make the appropriate allocations pursuant to Allocation 3 shall be deemed proportionately discharged. In the event that such bonds are paid and discharged prior to maturity, the foregoing obligation to make such appropriations and allocations shall be deemed to be proportionately discharged. </P>
<P>               (I)     In the event that other public and private funds in the future become available to construct or otherwise subsidize the low-income housing and related expenses hereinabove referred to, the Redevelopment Agency or the City may use such funds in lieu of the proceeds of the sale of the Redevelopment Agency low-income housing lease revenue bonds hereinabove described, and, to the extent that such funds become available and are utilized, the obligations of the Redevelopment Agency and the City to finance the low-income housing hereinabove described shall be deemed to be proportionately discharged. </P>
<P>               (J)     Once each year, as soon as practicable after June 30th, the Mayor shall ascertain the amount of money appropriated pursuant to this Allocation 3 which has not been expended or reserved for a specific use as provided herein and shall, following a period of public comment, prepare a report setting forth a program for expenditure of such money. </P>
<P>          (4)     Allocation Number 4 (War Memorial): To the War Memorial Department to be used to defray the cost of maintaining, operating and caring for the War Memorial buildings and grounds as described in Section
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Administrative%20Code%3Ar%3A39e1$cid=california$t=document-frame.htm$an=JD_27.3$3.0#JD_27.3'>27.3</A> of the San Francisco Administrative Code. </P>
<P>          (5)     Allocation Number 5 (Candlestick Point): To the Recreation and Park Department for Base Rental and Additional Rental as provided in the 1977 Amended Park Lease between the City and County of San Francisco and San Francisco Stadium, Inc. for the improvement and expansion of the Recreation Center located at Candlestick Point. </P>
<P>          (6)     Allocation Number 6 (Publicity/Advertising; Recurring Events): To the City Administrator for publicity and advertising purposes pursuant to the provisions of Section
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Charter%3Ar%3A66$cid=california$t=document-frame.htm$an=JD_3.104$3.0#JD_3.104'>3.104</A> of the Charter for cultural and promotional organizations and annual or regularly recurring parades, celebrations and street fairs, and to evaluate and review cultural, artistic or advertising programs funded pursuant to this Allocation Number 6 or Allocation Number 7. </P>
<P>          (7)     Allocation Number 7 (Publicity/Advertising; Nonrecurring Events): To the City Administrator to be used for publicity and advertising purposes pursuant to the provisions of Section
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Charter%3Ar%3A66$cid=california$t=document-frame.htm$an=JD_3.104$3.0#JD_3.104'>3.104</A> of the Charter for nonrecurring parades, celebrations and street fairs and for unforeseen special contingencies. </P>
<P>          (8)     Allocation Number 8 (Cultural Equity Endowment Fund): To the Arts Commission for cultural equity initiatives, commissions to individual creative artists in all disciplines, project grants to small and midsize arts organizations, and artspace initiatives or facilities acquisition programs. </P>
<P>          (9)     Allocation Number 9 (Asian Art Museum): To the Asian Art Museum of San Francisco for the operation and maintenance of the Museum. </P>
<P>          (10)     Allocation Number 10 (Fine Arts Museums): To the Fine Arts Museums of San Francisco for the operation and maintenance of the Museums. </P>
<P>          (11)     Allocation Number 11 (Cultural Centers): To the Arts Commission to support the operation, maintenance and programming of the City-owned community cultural centers to assure that these cultural centers remain open and accessible and remain vital contributors to the cultural life of the City. </P>
<P>          (12)     Allocation Number 12 (Protocol): To the Mayor to support the Mayor's Office of Protocol in their efforts to promote the City by hosting international visitors and delegations and by organizing events, trade missions, and other activities that promote San Francisco. This allocation shall expire at the end of fiscal year 1997-98 and shall not extend beyond that fiscal year. </P>
<P>     (c)     Each allocation for a purpose described in Subsection (b) shall be in the amount prescribed in the table below, subject to the adjustments and limitations prescribed in Subsection (d). </P>
<TABLE CELLPADDING=0 CELLSPACING=0 BORDER=0 WIDTH='100%'><TR><TD ALIGN=CENTER>
<TABLE CELLSPACING=0 BORDER=1 BORDERCOLOR=#000000 RULES=ALL WIDTH=701 CELLPADDING=4>
<TR><TD COLSPAN=2 WIDTH=413 VALIGN=TOP><P CLASS='TableHeader'>Allocation No.</P>
</TD><TD WIDTH=96 VALIGN=TOP><P CLASS='TableHeader'>1997  98</P>
</TD><TD WIDTH=96 VALIGN=TOP><P CLASS='TableHeader'>1998  99</P>
</TD><TD WIDTH=96 VALIGN=TOP><P CLASS='TableHeader'>1999  2000</P>
</TD></TR>
<TR><TD WIDTH=29 VALIGN=TOP><P>1.</P>
</TD><TD WIDTH=384 VALIGN=TOP><P>Convention Facilities</P>
</TD><TD WIDTH=96 VALIGN=TOP><P>$31,983,619</P>
</TD><TD WIDTH=96 VALIGN=TOP> </TD><TD WIDTH=96 VALIGN=TOP> </TD></TR>
<TR><TD WIDTH=29 VALIGN=TOP><P>2.</P>
</TD><TD WIDTH=384 VALIGN=TOP><P>Convention and Visitors Bureau</P>
</TD><TD WIDTH=96 VALIGN=TOP><P>$5,941,893</P>
</TD><TD WIDTH=96 VALIGN=TOP><P>$7,000,000</P>
</TD><TD WIDTH=96 VALIGN=TOP> </TD></TR>
<TR><TD WIDTH=29 VALIGN=TOP><P>3.</P>
</TD><TD WIDTH=384 VALIGN=TOP><P>Low-Income Housing: Yerba Buena Redevelopment Area</P>
</TD><TD WIDTH=96 VALIGN=TOP><P>$4,810,360</P>
</TD><TD WIDTH=96 VALIGN=TOP> </TD><TD WIDTH=96 VALIGN=TOP> </TD></TR>
<TR><TD WIDTH=29 VALIGN=TOP><P>4.</P>
</TD><TD WIDTH=384 VALIGN=TOP><P>War Memorial</P>
</TD><TD WIDTH=96 VALIGN=TOP><P>$7,473,309</P>
</TD><TD WIDTH=96 VALIGN=TOP> </TD><TD WIDTH=96 VALIGN=TOP> </TD></TR>
<TR><TD WIDTH=29 VALIGN=TOP><P>5.</P>
</TD><TD WIDTH=384 VALIGN=TOP><P>Candlestick Point</P>
</TD><TD WIDTH=96 VALIGN=TOP><P>$4,770,360</P>
</TD><TD WIDTH=96 VALIGN=TOP> </TD><TD WIDTH=96 VALIGN=TOP> </TD></TR>
<TR><TD WIDTH=29 VALIGN=TOP><P>6.</P>
</TD><TD WIDTH=384 VALIGN=TOP><P>Publicity/Advertising: Recurring Events (including Cultural Centers)</P>
</TD><TD WIDTH=96 VALIGN=TOP><P>$12,450,411</P>
</TD><TD WIDTH=96 VALIGN=TOP> </TD><TD WIDTH=96 VALIGN=TOP> </TD></TR>
<TR><TD WIDTH=29 VALIGN=TOP><P>7.</P>
</TD><TD WIDTH=384 VALIGN=TOP><P>Publicity/Advertising: Nonrecurring Events</P>
</TD><TD WIDTH=96 VALIGN=TOP><P>$191,427</P>
</TD><TD WIDTH=96 VALIGN=TOP> </TD><TD WIDTH=96 VALIGN=TOP> </TD></TR>
<TR><TD WIDTH=29 VALIGN=TOP><P>8.</P>
</TD><TD WIDTH=384 VALIGN=TOP><P>Cultural Equity Endowment Fund</P>
</TD><TD WIDTH=96 VALIGN=TOP><P>$1,722,843</P>
</TD><TD WIDTH=96 VALIGN=TOP> </TD><TD WIDTH=96 VALIGN=TOP> </TD></TR>
<TR><TD WIDTH=29 VALIGN=TOP><P>9.</P>
</TD><TD WIDTH=384 VALIGN=TOP><P>Asian Art Museum</P>
</TD><TD WIDTH=96 VALIGN=TOP><P>$1,565,873</P>
</TD><TD WIDTH=96 VALIGN=TOP> </TD><TD WIDTH=96 VALIGN=TOP> </TD></TR>
<TR><TD WIDTH=29 VALIGN=TOP><P>10.</P>
</TD><TD WIDTH=384 VALIGN=TOP><P>Fine Arts Museums</P>
</TD><TD WIDTH=96 VALIGN=TOP><P>$3,947,224</P>
</TD><TD WIDTH=96 VALIGN=TOP> </TD><TD WIDTH=96 VALIGN=TOP> </TD></TR>
<TR><TD WIDTH=29 VALIGN=TOP><P>11.</P>
</TD><TD WIDTH=384 VALIGN=TOP><P>Cultural Centers</P>
</TD><TD WIDTH=96 VALIGN=TOP><P>$600,000</P>
</TD><TD WIDTH=96 VALIGN=TOP><P>$900,000</P>
</TD><TD WIDTH=96 VALIGN=TOP><P>$1,800,000</P>
</TD></TR>
<TR><TD WIDTH=29 VALIGN=TOP><P>12.</P>
</TD><TD WIDTH=384 VALIGN=TOP><P>Protocol</P>
</TD><TD WIDTH=96 VALIGN=TOP><P>$1,500,000</P>
</TD><TD WIDTH=96 VALIGN=TOP><P>$0</P>
</TD><TD WIDTH=96 VALIGN=TOP><P>$0</P>
</TD></TR></TABLE>
</TD></TR></TABLE>
 <P>     (d)     Adjustments to and Limitations on Allocation Amounts. Notwithstanding the provisions of Subsection (c), the allocation amounts shall be subject to the following adjustments and limitations: </P>
<P>          (1)     Annual Adjustment: Prior to the calculation of any other adjustment prescribed in this Subsection (d), each amount prescribed in Subsection (c) shall be adjusted annually, commencing in fiscal year 1998-99, by the percentage increase or decrease in actual hotel tax revenues compared with the prior fiscal year; provided, however, that the amount of the annual adjustment pursuant to this Subparagraph (1) shall not exceed 10 percent. </P>
<P>          (2)     Limitation on Allocation Number 3 (Low-Income Housing in Yerba Buena Redevelopment Area): Unexpended monies appropriated pursuant to priority (E) of Allocation Number 3 shall be retained in a reserve fund which shall be allowed to accumulate in the maximum annual amount of $100,000 up to a maximum total amount of $1,000,000. </P>
<P>          (3)     Limitation on Allocation Number 6 (Publicity/Advertising; Recurring Events): Of the amount allocated for publicity and advertising for recurring events, $650,000 in 1997-1998; $800,000 in 1998-1999 and $400,000 in 1999-2000, thereafter adjusted by the annual adjustment provided in Subparagraph (1) of this paragraph, shall be allocated to the Arts Commission to support the City-owned community cultural centers. </P>
<P>          (4)     Adjustment to Allocation Number 6 (Publicity/Advertising; Recurring Events) and Allocation Number 11 (Cultural Centers): In fiscal year 1998-99 and thereafter, no amount allocated to support the City-owned community cultural centers shall be released to a cultural center unless: </P>
<P>               (A)     The Arts Commission has received and approved an annual report from the cultural center demonstrating that the cultural center has had an active community support board dedicated to community outreach, fundraising, and advocacy on behalf of the cultural center in the prior fiscal year. For purposes of this Section, an "active community support board" shall mean a board that has convened on at least six occasions during the year. </P>
<P>               (B)     The Arts Commission has received and approved an annual report from the cultural center demonstrating that the cultural center has, in the prior fiscal year, met the cultural center's revenue target from sources other than hotel tax revenues. For purposes of this Section, a cultural center's revenue target shall be at least 20 percent of the cultural center's total revenues, including hotel tax revenues, in fiscal year 1996-97 inflated annually by a rate of three percent or by the rate of growth in the cultural center's hotel tax revenues, whichever is lower. If the cultural center has not met its revenue target, the amount released to the cultural center shall be reduced in the following year by an amount equivalent to the difference between the revenue target and actual revenues collected from sources other than hotel tax revenues. All revenue calculations required to effectuate this limitation shall be certified by the Controller during the City's annual budget process. </P>
<P>               (C)     The Controller has performed a financial review of the cultural center within the previous four years. An initial financial review shall be performed for each cultural center by the end of fiscal year 1998-99. </P>
<P CLASS='History'>(Added by Ord. 300-97, App. 7/25/97; amended by Ord. 301-97, App. 7/25/97; Ord. 302-97, App. 7/25/97; Ord. 360-97, App. 9/5/97; Ord. 2-98, App. 1/16/98; Ord. 254-98, App. 7/31/98; Ord. 183-01, File No. 011174, App. 8/17/2001) </P>
<A NAME='JD_515.2'></A>
<a name="LPTOC15"></a><H3 CLASS='Section'><a href="javascript:void(0)" onclick="showUrl('JD_515.2')"><img src="/alp_templates/images/ui-bookmark.gif" width="16" height="16" alt="Bookmark" border="0"></a><span href="javascript:void(0)" onclick="showUrl('JD_515.2')" style="cursor: pointer">SEC. 515.2.  CALCULATION OF PERCENTAGE ALLOCATIONS UNDER SECTION 515.</span></H3>
<P>     (a)     Notwithstanding anything to the contrary in Section 515 of this Article, any and all percentage allocations set forth in Section 515 hereof shall be based on the sum of the monies for deposit to the Hotel Room Tax Fund plus the SFRA percentage (as defined hereinafter) of the total transient occupancy tax revenues actually received from the SFRA Project Areas regardless of whether such revenues are received by the City or the San Francisco Redevelopment Agency. The SFRA percentage shall equal the quotient of eight percent divided by the tax rate imposed by the City pursuant to Section
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.8$3.0#JD_502.8'>502.8</A> hereof. </P>
<P>     (b)     Notwithstanding Section 515(1) of this Article, the total amount to be allocated under Section 515(1) for each fiscal year shall be reduced by the amount of principal and interest (exclusive of any bond reserve payments) due and payable for that fiscal year on any outstanding agency bonds, as defined in Section
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.8$3.0#JD_502.8'>502.8</A>(c) hereof. </P>
<P>     (c)     Section
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_515.2$3.0#JD_515.2'>515.2</A> shall remain in effect so long as Section
<A HREF='/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_502.8$3.0#JD_502.8'>502.8</A> of this Article remains in effect.</P>
<P CLASS='History'>(Added by Ord. 227-94, App. 6/9/94)</P>
<A NAME='JD_Article8'></A><P CLASS='Article-Deleted'>ARTICLE 8:<BR />
[RESERVED]</P>


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
html.make_links_absolute('http://www.amlegal.com/nxt/gateway.dll?f=id$id=San%20Francisco%20Business%20and%20Tax%20Regulations%20Code%3Ar%3A595$cid=california$t=document-frame.htm$an=JD_Article7$3.0#JD_Article7')
observed = lib.sections(html)

def test_count():
    n.assert_equal(len(observed), 15)
