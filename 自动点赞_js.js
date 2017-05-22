function clickGood(){
	let li = jQuery("ul#feed_friend_list").find("li");
	let a = jQuery(li[1]).find(".qz_like_btn_v3");
	if(jQuery(a).attr("data-clicklog")=='like'){
		let i = jQuery(a).find(".fui-icon");
		i.click();
	}
}
clickGood();
function myrefresh(){  
    document.getElementById("feed_friend_refresh").click();  
    console.log("刷新成功");
    setTimeout(function(){
    	clickGood(); 
    },2000);
    
    setTimeout(function(){
    	myrefresh();
    },30000);  
}  
myrefresh();


let a = jQuery(li[1]).find(".qz_like_btn_v3");if(jQuery(a).attr("data-clicklog")=="like"){let i = jQuery(a).find(".fui-icon");i.click();