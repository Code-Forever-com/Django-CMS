const $nav_side = $(".dash-nav-side");
const $nav_side_text = $(".aside-menu-text");
const $close_menu = $("#close-menu");
$close_menu.click(function (e) {

    $close_menu.children("i").toggleClass("fa-arrow-right");
    if ($nav_side.css("flex") == "0 0 40px") {
        $nav_side.css("flex", "0 0 150px");
        setTimeout(function () {
            $nav_side_text.toggle();
        }, 600);
    } else {
        $nav_side.css("flex", "0 0 40px");
        $nav_side_text.toggle();
    }
});

const $cms_tr = $(".cms-table .cms-body .cms-tr-container");

$cms_tr.click(function (e) {
    $(e.currentTarget.lastElementChild).toggle();
})