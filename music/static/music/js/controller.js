

$(document).ready(function () {
    //initClickListeners();
});

function initClickListeners()
{
    $("#show_login").click(function () {
        $("#register").hide();
        $("#login").show();
        return false;
    });

    $("#show_register").click(function () {
        $("#login").hide();
        $("#register").show();
        return false;
    });
}