/** cookie operate **/
var cookieOperate = /** @class */ (function () {
    function cookieOperate() {
    }

    cookieOperate.prototype.getCookie = function (cname) {
        var name = cname + "=";
        var ca = document.cookie.split(';');
        for (var i = 0; i < ca.length; i++) {
            var c = ca[i];
            while (c.charAt(0) == ' ')
                c = c.substring(1);
            if (c.indexOf(name) != -1)
                return c.substring(name.length, c.length);
        }
        return "";
    };
    cookieOperate.prototype.setCookie = function (cname, cvalue, exdays) {
        var d = new Date();
        d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
        var expires = "expires=" + d.toUTCString();
        document.cookie = cname + "=" + cvalue + "; " + expires;
    };
    return cookieOperate;
}());

$(document).ready(function () {
    // 获取购物车数目
    $.ajax({
        type: 'GET',
        url: '/shop/getcartnum1/',
         success: function (res) {
            if (res.recode) {
                $('#show_count').text(res.data.allcart);
            } else {
                if (res.data) {
                    alert(res.data.error);
                };
            }
        }
    })

});