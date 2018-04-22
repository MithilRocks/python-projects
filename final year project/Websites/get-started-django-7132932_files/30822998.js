/* AG-master 13.09.28-32 (2013-09-28 13:16:16 GMT) */
rsinetsegs=['A08721_10253','A08721_50225','A08721_50239','A08721_50179','A08721_50144','A08721_50198','A08721_0'];
var rsiExp=new Date((new Date()).getTime()+2419200000);
var rsiDom='.creativebloq.com';
var rsiSegs="";
var rsiPat=/.*_5.*/;
for(x=0;x<rsinetsegs.length;++x){if(!rsiPat.test(rsinetsegs[x]))rsiSegs+='|'+rsinetsegs[x];}
document.cookie="asi_segs="+(rsiSegs.length>0?rsiSegs.substr(1):"")+";expires="+rsiExp.toGMTString()+";path=/;domain="+rsiDom;
document.cookie="rsi_segs="+(rsiSegs.length>0?rsiSegs.substr(1):"")+";expires="+rsiExp.toGMTString()+";path=/;domain="+rsiDom;
if(typeof(DM_onSegsAvailable)=="function"){DM_onSegsAvailable(['A08721_10253','A08721_50225','A08721_50239','A08721_50179','A08721_50144','A08721_50198','A08721_0'],'a08721');}