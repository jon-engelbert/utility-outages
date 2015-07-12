import scrapy
import json
import os

class DmozSpider(scrapy.Spider):
    name = "utility"
    # allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://173.202.239.131:82/",
        "http://162.255.126.250:89/",
        "http://ebill.wwvremc.com/oms/outageMap",
        "http://204.116.73.46/",
        "http://209.212.41.13:81/",
        "http://209.142.137.161/",
        "http://216.174.162.32/OMSWebMap/Map/OMSWebMap.htm",
        # "http://216.229.71.219/", not found??
        "http://216.229.88.141/omswebmap/Map/OMSWebMap.htm?clientKey=undefined",
        "http://216.47.203.35/OMSWebMap/Map/OMSWebMap.htm",
        "http://216.59.205.228/",
        "http://64.40.223.70/OMSWebMap/Map/OMSWebMap.htm?clientKey=undefined",
        "http://66.63.235.29/Outages/",
        "http://69.151.48.214/",
        "http://74.122.17.102/",
        "http://74.122.17.88/",
        "http://74.41.135.190:7575/",
        "http://aecoop.org/outage-map/",
        "http://apps.ameren.com/outage/outagemap.aspx?state=MO",
        "http://apps.coned.com/stormcenter_external_oru/default.html",
        "http://apps.emeramaine.com/about/outages/Outage_Map.cfm",
        "http://bemc.maps.sienatech.com/",
        "http://bremco.maps.sienatech.com/",
        "http://caec.coop/electric-service/current-outages/",
        "http://cecdata.com/outageMap.html",
        "http://cherrylandelectric.coop/outage-center/",
        "http://choptank.maps.sienatech.com/",
        "http://cmlpoms.concordma.gov/OMSWebMap/Map/OMSWebMap.htm",
        "http://crecoutageviewer.crec.coop:82/",
        "http://dec.maps.sienatech.com/",
        "http://demco.maps.sienatech.com/",
        "http://dme.maps.arcgis.com/apps/Viewer/index.html?appid=8e2974bf8ee943dfa4016e85571f5624",
        "http://ebill.canadianvalley.org/oms/outageMap",
        "http://ebill.cec.coop/OMSWebMap/Map/OMSWebMap.htm",
        "http://ebill.kayelectric.coop/oms/outageMap",
        "http://ebill.loganrec.com/oms/outageMap",
        "http://ebill.lrecok.coop/oms/outageMap",
        "http://ebill.mcec.org/oms/outageMap",
        "http://ebill.nwdakota.com/oms/outageMap",
        "http://ebill.pvrea.com/oms/outageMap",
        "http://ebill.wste.coop/oms/outageMap",
        "http://ebill.wwvremc.com/oms/outageMap",
        "http://electric_outage.lpandl.com/",
        "http://energy.gov/sepa/maps/southeastern-power-administration",
        "http://entergy.com/storm_center/outages.aspx",
        "http://fvutil.com/news/outage/",
        "http://gccea.coopwebbuilder2.com/content/outage-map",
        "http://gis.centerpointenergy.com/outagetracker/",
        "http://gis.fourcty.org/pub/map.html",
        "http://gis.ouc.com/mobiledetect.html",
        "http://gisservices.oremc.co/FlexDebug/External/eMaps/",
        "http://highwestenergy.com/outage-center",
        "http://host.linncountyrec.com/outagemap.aspx",
        "http://iplmap.indepmo.org/",
        "http://joemc.maps.sienatech.com/",
        "http://lec.maps.sienatech.com/",
        "http://m.gru.com/emergency/electric.jsp",
        "http://mapping.tec.coop/MobileBrowser/Map.htm",
        "http://mcdonoughpower.com/safety-outages/outage-updates/",
        "http://mi.lcp.coop:82/",
        "http://mvec.com/energy-center/live-outage-info",
        "http://ompa.com/outages/",
        "http://oms.coastalemc.com/OMSWebMap/Map/OMSWebMap.htm",
        "http://oms.decaturutilities.com:85/",
        "http://oms.hwe.coop/",
        "http://oms.tcectexas.com/",
        "http://omsviewer.southaec.com/",
        "http://outage.banderaelectric.com/",
        "http://outage.bgenergy.com/",
        "http://outage.bluebonnetelectric.coop:82/",
        "http://outage.clintonub.com/",
        "http://outage.covington.coop/",
        "http://outage.crawfordelec.com/",
        "http://outage.excelsioremc.com:8181",
        "http://outage.fallriverelectric.com/omswebmap/",
        "http://outage.fallriverelectric.com/omswebmap/Map/OMSWebMap.htm",
        "http://outage.farmersrecc.com/",
        "http://outage.fecc.coop/",
        "http://outage.flathead.coop:8181/",
        "http://outage.itasca-mantrap.com/",
        "http://outage.jec.coop:83/",
        "http://outage.kwh.com/",
        "http://outage.mvea.org/",
        "http://outage.mvec.net/",
        "http://outage.neelectric.com/",
        "http://outage.nueceselectric.org/",
        "http://outage.preco.coop/",
        "http://outage.rayleemc.com:82/",
        "http://outage.samhouston.net:89/",
        "http://outage.sec.coop:8181/",
        "http://outage.tcec.com/",
        "http://outage.tvepa.com:82/",
        "http://outage.united-cs.com/",
        "http://outage.whe.org/",
        "http://outage.wmeco.com/outage/outagemap.aspx",
        "http://outagecenter.pseg.com/external/default.html",
        "http://outageinfo.lbwl.com/",
        "http://outagemap.cecmo.com/",
        "http://outagemap.clayelectric.com/",
        "http://outagemap.coserv.com/external/default.html",
        "http://outagemap.cpsenergy.com/CPSStaticMapsEXT/CPSStaticMapV2_EXT.html",
        "http://outagemap.duke-energy.com/ncsc/default.html",
        "http://outagemap.duke-energy.com/ohky/default.html",
        "http://outagemap.gcec.com/",
        "http://outagemap.georgiapower.com/external/default.html?hp=tm_po_view_outage_map",
        "http://outagemap.gibsonemc.com/",
        "http://outagemap.gulfpower.com/external/default.html?ghp=s1_bx3_link3",
        "http://outagemap.jocarroll.com/",
        "http://outagemap.kcpl.com/external/default.html",
        "http://outagemap.lrec.coop/",
        "http://outagemap.mississippipower.com/external/default.html",
        "http://outagemap.nyseg.com/ny/?style=newyork",
        "http://outagemap.rge.com/ny/?style=rge",
        "http://outagemap.trimble.com/EECA/OutageMap.html",
        "http://outagemap.trimble.com/skrecc/",
        "http://outages.4county.org:8181/",
        "http://outages.barcelectric.com:83/",
        "http://outages.bcec.com:89/",
        "http://outages.btutilities.com/",
        "http://outages.cstx.gov:83/",
        "http://outages.firstenergycorp.com/mdwv.html",
        "http://outages.firstenergycorp.com/nj.html",
        "http://outages.firstenergycorp.com/oh.html",
        "http://outages.firstenergycorp.com/pa.html",
        "http://outages.gvec.org/",
        "http://outages.heartlandremc.com:89/",
        "http://outages.lumbeeriver.com/",
        "http://outages.meckelec.org:81/",
        "http://outages.navasotavalley.com:85/",
        "http://outages.nnec.coop/",
        "http://outages.nppd.com/external/default.html",
        "http://outages.nwecok.org/omswebmap/Map/OMSWebMap.htm",
        "http://outages.ocalafl.org/",
        "http://outages.polkburnett.com/",
        "http://outages.sdrea.coop/",
        "http://outages.spepa.com/",
        "http://outages.sussexrec.com/",
        "http://outages.svec-coop.com/",
        "http://outageview.chelco.com:8088/",
        "http://outageviewer.becsc.com:88/",
        "http://outageviewer.gocolumbiamo.com/",
        "http://outageviewer.santee.org:9600/",
        "http://ozarkborder.org/current_outages.html",
        "http://peopleselectric.coop/custom/index.php",
        "http://pge.com/myhome/outages/outage/",
        "http://ppec.coop/territory-and-outage-maps/",
        "http://prepared.dixieepa.com/",
        "http://provo.org/departments/power/current-outages-map",
        "http://publicweb.nli.coop/",
        "http://sciremc.maps.sienatech.com/",
        "http://stormcenter.booneelectric.coop/default.html",
        "http://stormcenter.lge-ku.com/default.html",
        "http://stormcenter.oncor.com/",
        "http://stormcenter.smeco.coop/",
        "http://stormcenter3.csu.org.s3.amazonaws.com/default.html",
        "http://stormcentral.cenhud.com/default.aspx",
        "http://tools.sensus.com/IMS/default.aspx?id=56",
        "http://unitil.com/outage-center/electric-outage-map",
        "http://vtoutages.com/",
        "http://72.29.36.60:8081/"
        # "http://washingtonemc.com/%20%2Aclick%20on%20%22outage%20viewer%22",
        "http://72.29.36.60:8081/",
        "http://web.tdpud.org/TDPUDStormMap/",
        "http://ww2.ambitenergy.com/contact-ambit-energy",
        "http://ww3.oppd.com/power-outage-map/",
        "http://www.amicalolaemc.com/report-an-outage/",
        # "http://www.arcgis.com/home/webmap/viewer.html?webmap=bde962b19fa1480db788c0ef4369a8b4&extent=-84.2209%2C33.7905%2C-81.7778%2C34.7697",
        "http://www.atlanticcityelectric.com/outage/",
        "http://www.bcremc.com/outages/",
        "http://www.blackhillspower.com/outages",
        "http://www.ccecaomsview.com/omswebmap/Map/OMSWebMap.htm?clientKey=undefined",
        "http://www.cfec.com/#!outage-map/sitepage_17",
        "http://www.championenergyservices.com/customer-service/power-outage/",
        "http://www.cityofpaloalto.org/gov/depts/utl/residents/outages/utilities_outage_map.asp",
        "http://www.cityutilities.net/outage/outagemap.htm",
        "http://www.clarkpublicutilities.com/index.cfm/safety-outages/power-outages/outage-map/",
        "http://www.consumersenergy.com/outagemap",
        "http://www.cornbeltenergy.com/outages/outage-updates.html",
        "http://www.cuivre.com/NewsCenter/LiveOutageViewer/tabid/129/Default.aspx",
        "http://www.cullmanecoutages.com/works.html",
        "http://www.cvec.coop/content/outage-reporting",
        "http://www.cvecoop.com/outages/outages.php",
        # "http://www.dmea.com:5050/",  timed out
        "http://www.dpandl.com/customer-service/outage-center/report-an-outage/",
        "http://www.dteenergy.com/map/outage.html",
        "http://www.e-co-op.com/outagemap/out_map.html",
        "http://www.e-u.cc/CustomerOutagePage.html",
        "http://www.ecirec.coop/webfront/more-info/?page_id=231",
        "http://www.empiredistrict.com/Outages/OutageMap.aspx",
        "http://www.energysterling.com/energy_services.asp#tabs-4",
        "http://www.epelectric.com/outage-map",
        "http://www.etrviewoutage.com/external/ar.aspx",
        "http://www.etrviewoutage.com/external/la.aspx",
        "http://www.etrviewoutage.com/external/ms.aspx",
        "http://www.etrviewoutage.com/external/nola.aspx",
        "http://www.etrviewoutage.com/external/tx.aspx",
        "http://www.firelandsec.com/content/current-outages",
        "http://www.frenchbroademc.com/outagemap.cfm",
        "http://www.gosemo.com/content/outage-center",
        "http://www.gradyemc.com/Outage%20Information.html",
        "http://www.gtlakes.com/storm-central/",
        "http://www.gvp.org/content/outage-map",
        "http://www.hannibalbpw.org/outage-reports/",
        "http://www.heartland-rec.com/content/outage-map",
        "http://www.hillsdalebpu.com/outage-information/",
        "http://www.iowarec.org/outages",
        "http://www.iowarec.org/outages/",
        "http://www.ismymeteron.com/",
        "http://www.jwemc.org/current-outages/",
        "http://www.kec.com/content/power-outage-updates",
        "http://www.kiamichielectric.org/content/current-outages",
        "http://www.lcec.coop/content/outage-information",
        "http://www.les.com/report-outage#map-anchor",
        "http://www.libertyutilities.com/east/electricity/outage_central/outage_map.html",
        "http://www.magicvalley.coop/map/outage",
        "http://www.mge.com/safety-outages/power-outages/outage-map/index.htm",
        "http://www.midamericanenergy.com/storm/OutageWatch_2013/dsk.html",
        "http://www.mnpower.com/OutageCenter/OutageMap",
        "http://www.mohaveelectric.com/content/outage-center",
        "http://www.mtemc.com/status/status.cfm",
        "http://www.noblesolutions.com/about-us/index.html",
        "http://www.northwesternrec.com/content/storm-center-0",
        "http://www.oecc.com/view-outage",
        "http://www.ohioruralelectric.coop/outages/outage-map/",
        "http://www.okcoop.org/outages",
        "http://www.oru.com/energyandsafety/storms/outagemapredirect/index.html",
        "http://www.outagecentral.com/showOutageurl/148005",
        "http://www.outagecentral.com/showOutageurl/28142",
        "http://www.outageentry.com/CustomerFacingApp/map.php?clientid=ALCOA",
        "http://www.outageentry.com/CustomerFacingApp/map.php?clientid=CDE",
        "http://www.outageentry.com/CustomerFacingApp/map.php?clientid=CHICKASAW",
        "http://www.outageentry.com/CustomerFacingAppJQM/outage.php?clientid=WALTON",
        "http://www.outageentry.com/dvOSM/dvOSM2.php?Client=COH",
        "http://www.outageentry.com/dvOSM/dvOSM2.php?Client=ROCK",
        "http://www.outageentry.com/dvOSM/dvOSM2.php?Client=prvepa",
        "http://www.outageentry.com/dvOSM/dvOutages.php?Client=svec",
        "http://www.outageentry.com/dvOSM4/dvOSM4.php?Client=ARKVALLEY",
        "http://www.outageentry.com/dvOSM4/dvOSM4.php?Client=wise",
        "http://www.outagemap-xcelenergy.com/outagemap/",
        "http://www.outagemap-xcelenergy.com/outagemap/?zipcode=20585",
        "http://www.outagemap-xcelenergy.com/outagemap/?zipcode=75219",
        "http://www.ozarkelectric.com/outage_center/current_outages.html",
        "http://www.pcec.coop/services/platte-clay-area-outage-map/",
        "http://www.pepco.com/pages/connectwithus/outages/outagemaps.aspx",
        "http://www.pge.com/myhome/outages/outage/",
        "http://www.pioneerelectric.com/content/outage-map",  # http://209.142.137.161/
        "http://www.psrec.coop/service-area.php",   # outages on this map?
        "http://www.pud-ri.org/outages-safety/outage-map",
        "http://www.randolphemc.com/content/randolph-emc-outage-map",
        "http://www.remc.com/storm-center/outage-map/",
        "http://www.roanokeelectric.com/content/outage-map-0",
        "http://www.rock.coop/content/current-reported-outages",
        "http://www.rpu.org/contact-us/power-outages.html",
        "http://www.sawnee.com/content/current-outages",
        "http://www.secostormcenter.com/StormCenter.aspx",
        "http://www.seiec.com/outage-map",
        "http://www.slemco.com/site.php?pageID=350",
        "http://www.southcentralpower.com/ow/ow_map.aspx",
        "http://www.southernriversenergy.com/%20%2Aclick%20on%20%22outage%20viewer%22",
        "http://www.ssemc.com/etc/outages.asp",
        "http://www.stec.org/outage2.aspx",
        "http://www.surprisevalleyelectric.org/content/outage-map",
        "http://www.swce.coop/operations/outagemap.php",
        "http://www.tampaelectric.com/residential/outages/outagemap/",
        "http://www.tcemc.org/outages/",
        "http://www.tclp.org/Mutual/ReportOutage/Residential",
        "http://www.threeriverselectric.com/page.php?p=2563",
        "http://www.tidelandemc.com/outageMap.aspx",
        "http://www.tipmont.org/outages",
        "http://www.ugi.com/portal/page/portal/UGI/Outage_Center/Outage_Map",
        "http://www.uppco.com/outagesummary/view/outagegrid.aspx",
        "http://www.vea.coop/sites/vea.coopwebbuilder.com/files/page-images/service_area_boundary_map.jpg",
        "http://www.vernonelectric.org/content/outages",
        "http://www.wcec.org/index.php/outage-center/current-outages/",
        "http://www.we-energies.com/outagemapext/",
        "http://www.westcentralelectric.coop/content/outage-map",
        "http://www.westflorida.coop/outage_map/",
        "http://www.wisconsinpublicservice.com/outagesummary/view/outagegrid.aspx",
        "http://www.xcelenergy.com/Outages",
        "http://www.yorkelectric.net/outages/",
        "http://www2.ngemc.com:81/",
        "https://aeptexas.com/outages/outageMap.aspx",
        "https://css.jcpb.com/woViewer/mapviewer.html?config=Outage%2BWeb%2BMap",
        "https://ebill.adamsec.com/mapviewer/mapviewer.html?config=Outage%2BWeb%2BMap",
        "https://ebill.alfalfaelectric.com/woViewer/mapviewer.html?config=Outage%2BWeb%2BMap",
        "https://ebill.bremc.com/woViewer/mapviewer.html?config=Outage%2BWeb%2BMap",
        "https://ebill.butler.coop/woViewer/mapviewer.html?config=Outage%2BWeb%2BMap",
        "https://ebill.butlerrural.coop/oms/outageMap",
        "https://ebill.cceci.com/woViewer/mapviewer.html?config=Outage%2BWeb%2BMap",
        "https://ebill.cecoop.com/woViewer/mapviewer.html?config=Outage%2BWeb%2BMap",
        "https://ebill.central.coop/oms/outageMap",
        "https://ebill.claverack.com/oms/outageMap",
        "https://ebill.co-mo.coop/woViewer/mapviewer.html?config=Outage%2BWeb%2BMap",
        "https://ebill.comelec.coop/oms/outageMap",
        "https://ebill.cumberlandvalley.coop/woViewer/mapviewer.html?config=Outage%2BWeb%2BMap",
        "https://ebill.cwremc.com/woViewer/mapviewer.html?config=Outage%2BWeb%2BMap",
        "https://ebill.darkerec.com/oms/outageMap",
        "https://ebill.douglaselectric.com/woViewer/mapviewer.html?config=Outage%2BWeb%2BMap",
        "https://ebill.dsec.org/woViewer/mapviewer.html?config=Outage%2BWeb%2BMap",
        "https://ebill.ecec.com/oms/outageMap",
        "https://ebill.frontier-power.com/oms/outageMap",
        "https://ebill.grayson-collin.coop/woViewer/mapviewer.html?config=Outage%2BWeb%2BMap",
        "https://ebill.holycross.com/oms/outageMap",
        "https://ebill.homeworks.org/woViewer/mapviewer.html?config=Outage%2BWeb%2BMap",
        "https://ebill.hwecoop.com/woViewer/mapviewer.html?config=Outage%2BWeb%2BMap",
        "https://ebill.iecok.com/oms/outageMap",
        "https://ebill.kcelectric.coop/oms/outageMap",
        "https://ebill.ljec.coop/oms/outageMap",
        "https://ebill.medinaec.org/oms/outageMap",
        "https://ebill.midlandpower.coop/outageMap",
        "https://ebill.midlandpower.coop/woViewer/mapviewer.html?config=Outage%2BWeb%2BMap",
        "https://ebill.midwestrec.com/woViewer/mapviewer.html?config=Outage%2BWeb%2BMap",
        "https://ebill.mjmec.coop/oms/outageMap",
        "https://ebill.mlecmn.net/woViewer/mapviewer.html?config=Outage%2BWeb%2BMap",
        "https://ebill.norrisppd.com/woViewer/mapviewer.html?config=Outage%2BWeb%2BMap",
        "https://ebill.osagevalley.com/oms/outageMap",
        "https://ebill.ozarksecc.com/woViewer/mapviewer.html?config=Outage%2BWeb%2BMap",
        "https://ebill.piercepepin.com/woViewer/mapviewer.html?config=Outage%2BWeb%2BMap",
        "https://ebill.ppec.coop/woViewer/mapviewer.html?config=Outage%2BWeb%2BMap",
        "https://ebill.rgec.com/woViewer/mapviewer.html?config=Outage%2BWeb%2BMap",
        "https://ebill.rrvrea.com/woViewer/mapviewer.html?config=Outage%2BWeb%2BMap",
        "https://ebill.sanpatricioelectric.org/oms/outageMap",
        "https://ebill.scaec.com/woViewer/mapviewer.html?config=Outage%2BWeb%2BMap",
        "https://ebill.seiremc.com/oms/outageMap",
        "https://ebill.shelbyelectric.coop/woViewer/mapviewer.html?config=Outage%2BWeb%2BMap",
        "https://ebill.sweci.com/woViewer/mapviewer.html?config=Outage%2BWeb%2BMap",
        "https://ebill.swrea.com/oms/outageMap",
        "https://ebill.teammidwest.com/woViewer/mapviewer.html?config=Outage%2BWeb%2BMap",
        "https://ebill.theenergycoop.com/oms/outageMap",
        "https://ebill.toddwadena.coop/outagemap/",
        "https://ebill.trico.org/woViewer/mapviewer.html?config=Outage%2BWeb%2BMap",
        "https://ebill.tricountycoop.com/oms/outageMap",
        "https://ebill.unitedpa.com/oms/outageMap",
        "https://ebill.unitedpower.com/outage_external/",
        "https://ebill.urecc.coop/oms/outageMap",
        "https://ebill.vvec.com/woViewer/mapviewer.html?config=Outage%2BWeb%2BMap",
        "https://ebill.wemc.com/woViewer/mapviewer.html?config=Outage%2BWeb%2BMap",
        "https://ebill.westriver.com/oms/outageMap",
        "https://ebill.whiteriver.org/woViewer/mapviewer.html?config=Outage%2BWeb%2BMap",
        "https://ebill1.navopache.org/woViewer/mapviewer.html?config=Outage%2BWeb%2BMap",
        "https://fmcs.ebill.coop/outageMap",
        "https://info.mcleodcoop.com/oms/outageMap",
        "https://mss.pioneerec.com/woViewer/mapviewer.html?config=Outage%2BWeb%2BMap",
        "https://my.austinenergy.com/outages/",
        "https://myaccount.srpnet.com/MyAccount/Outages/public",
        "https://oge.com/wps/portal/oge/outages/systemwatch/%21ut/p/a1/pZFRa4MwEMe_in3Zo5fF1vY11VJqoWtloS4vI4ZMQ42RKAv99otjT2O6we7t4Pfj7v4HDApgLX9XFR-UaXkz9ix-3WCUoMMSZ3ucxYgk-fMa0xwjGnngxQNoogj65h_xDpFjml5W5_TxEMVf_hRwWv5t_pS__afvF_zFvwL7ROYSmM1gPHEW8DdkwKrGlP4f1",
        "https://pyxis-oms.com/OutageMap/AgraliteOutageMap.html",
        "https://pyxis-oms.com/OutageMap/MeekerOutageMap.htm",
        "https://pyxis-oms.com/OutageMap/OutageMap.htm",
        "https://recc.ebill.coop/outageMap",
        "https://rrelectric.ebill.coop/outageMap",
        "https://s-webserv.fecelectric.com/farmersec/outagecenter/",
        "https://swepco.com/outages/outageMap.aspx",
        "https://taylorelectric.ebill.coop/woViewer/mapviewer.html?config=Outage%2BWeb%2BMap",
        "https://twitter.com/BroadRiverCoop",
        "https://twitter.com/Newbern_Tn",
        "https://wss.greenmountainpower.com/customers/outages/",
        "https://www.aepaccount.com/zipr/StormsAndOutages/Default.aspx",
        "https://www.aepohio.com/outages/outageMap.aspx",
        "https://www.aepohio.com/outages/report/",
        "https://www.aeptexas.com/outages/outageMap.aspx",
        "https://www.appalachianpower.com/outages/outageMap.aspx",
        "https://www.appalachianpower.com/outages/report/",
        "https://www.avistautilities.com/safety/outages/_layouts/avista/transactions/ViewOutages.aspx?map=1",
        "https://www.bentonrea.org/outagemap.html",
        "https://www.comed.com/_layouts/comedsp/OutageMap.aspx",
        "https://www.dom.com/residential/dominion-virginia-power/outage-center/outages-by-region-and-maps",
        "https://www.duquesnelight.com/forYourHome/outagesAndSafety/ViewCurrentOutages.cfm",
        "https://www.ecemn.com/woViewer/mapviewer.html?config=Outage%2BWeb%2BMap",
        "https://www.empiredistrict.com/Outages/OutageMap.aspx",
        "https://www.epb.net/outages/",
        "https://www.eversource.com/Content/general/residential",
        "https://www.firstenergycorp.com/content/customer/outages_help/current_outages_maps.html",
        "https://www.firstenergycorp.com/outages_help/current_outages_maps.html",
        "https://www.idahopower.com/Outages/map/default.cfm",
        "https://www.indianamichiganpower.com/outages/outageMap.aspx",
        "https://www.iowarec.org/outages/",
        "https://www.jea.com/Outage_Center/Outage_Map/",
        "https://www.kentuckypower.com/outages/outageMap.aspx",
        "https://www.ladwp.com/ladwp/faces/header/outageinformation",
        "https://www.laurenselectric.com/outage-center/",
        "https://www.mariettaga.gov/city/mpw/power/outages",
        "https://www.mblp.org/outages.php?report",
        "https://www.nvenergy.com/outage/",
        "https://www.outageentry.com/CustomerFacingApp/map.php?clientid=ADAMS",
        "https://www.outageentry.com/CustomerFacingApp/map.php?clientid=NEMEPA",
        "https://www.peoplesrec.com/content/outage-map",
        "https://www.pnm.com/search-an-outage",
        "https://www.pplelectric.com/my-account/outage-center/outage-map.aspx",
        "https://www.sce.com/wps/portal/home/outage-center/outage-map/%21ut/p/b1/rVTbUsIwEP0VXnjMZNMkTXgsFUtRuQgi7QsTQoNVWm6F0b-3XGZQZrhqnrLJ7pmzZ0-CQ9zDYapW8Uhl8SRV43Uc2n0iPafqt8H3RBXAf3YJca2WBcDzhCBPgCPLgU19yYNKtdbI6zstCj5tQb3tOBTAxq84xKFOs2n2hoOFjvp6kmZRmvWjtAi",
        "https://www.sceg.com/outages-emergencies/power-outages/outage-map",
        "https://www.stearnselectric.org/outage-center/view-current-outages/",
        "https://www.swepco.com/outages/outageMap.aspx",
        "https://www.tep.com/outage/map/",
        "https://www.wrec.net/outage-map",
        "https://www1.nationalgridus.com/PowerOutageMap",
        "https://www2.ameren.com/common/OutageStatus.aspx"    
    ]

    def parse_outageviewer(self, response):
        filenameList = response.url.split("/")[1:]
        filename = "_".join(filenameList)
        self.logger.info('A response from %s just arrived in parse_outageviewer!', response.url)
        json_dict = json.loads(response.body_as_unicode())
        # outages = json_dict['outages']
        # if len(outages) > 0:
        with open("json_outageviewer_" + filename + ".txt", 'wb') as f:
            f.write("full text: " + str(json_dict))
            for sub_dict in json_dict['outages']:
                f.write("\n")
                f.write("outages section: " + str(sub_dict))
                f.write("\n")
                f.write("number of outages: " + str(sub_dict['customers_out_now']))

    def parse(self, response):
        is_found = False

        filenameList = response.url.split("/")[1:]
        filename = "_".join(filenameList)

        total_text = response.xpath("//*[contains(., 'Total')]/ancestor::table")
        total_list = total_text.extract()
        if len(total_list) > 0:
            is_found = True
            with open("totaltable_" + filename + ".txt", 'wb') as f:
                f.write(response.url)
                f.write(repr(total_list))

        total_text = response.xpath("//title[contains(.,'Outage Viewer')]") 
        total_list = total_text.extract()
        if len(total_list) > 0:
            is_found = True
            with open("outageviewer.txt", 'a') as f:
                f.write(filename +  "/index.php?action=get_viewer_data\n")
            if response.url[-1] != '/':
                response.url += '/'
            yield scrapy.Request(response.url + "index.php?action=get_viewer_data", callback=self.parse_outageviewer)
                # make_requests_from_url(response.url + "index.php?action=get_viewer_data")


        total_text = response.xpath("//div[@id='scontrols']") 
        total_list = total_text.extract()
        if len(total_list) > 0:
            is_found = True
            filename = "storm_center_" + filename + ".txt"
            filename2 = "sc_selenium_" + filename + ".txt"
            with open(filename, 'wb') as f:
                f.write(response.url)
                f.write(repr(total_list))
            os.system("python ~/projects/utility-outage/main.py -i " + response.url + " -o " + filename2)

        total_text = response.xpath("//div[@id='customers_out']") 
        total_list = total_text.extract()
        if len(total_list) > 0:
            is_found = True
            with open("div_customersout_" + filename + ".txt", 'wb') as f:
                f.write(response.url)
                f.write(repr(total_list))

        total_text = response.xpath("//div[@id='map_canvas']") 
        total_list = total_text.extract()
        if len(total_list) > 0:
            is_found = True
            with open("div_mapcanvas_" + filename + ".txt", 'wb') as f:
                f.write(response.url)
                f.write(repr(total_list))

        total_text = response.xpath("//iframe") 
        total_list = total_text.extract()
        if len(total_list) > 0:
            is_found = True
            with open("iframe_" + filename + ".txt", 'wb') as f:
                f.write(response.url)
                f.write(repr(total_list))

        if not is_found:
            with open("not_found_" + filename + ".txt", 'wb') as f:
                f.write("not_found_" +response.url)
        # total_text = response.xpath("//ul/li[text()[contains(.,'Total')]]/ancestor") 
        # total_list = total_text.extract()
        # if len(total_list) > 0:
        #     with open(filename + "_ul2.txt", 'wb') as f:
        #         f.write(response.url)
        #         f.write(repr(total_list))
        # total_text = response.xpath("//ol//li[contains(.,'Total')]/ancestor") 
        # total_list = total_text.extract()
        # if len(total_list) > 0:
        #     with open(filename + "_ol1.txt", 'wb') as f:
        #         f.write(response.url)
        #         f.write(repr(total_list))
        # total_text = response.xpath("//ol//li[text()[contains(.,'Total')]]/ancestor") 
        # total_list = total_text.extract()
        # if len(total_list) > 0:
        #     with open(filename + "_ol2.txt", 'wb') as f:
        #         f.write(response.url)
        #         f.write(repr(total_list))

# http://173.202.239.131/
# //*[@id="viewer-totals"]/li[1]/text()
# //*[@id="CountiesTable"]/table/tfoot/tr/th[2]/b