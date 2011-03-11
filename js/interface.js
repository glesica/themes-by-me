// *****
// Interface code for Nice Layout
// Author: George Lesica <glesica@gmail.com
// *****

// *****
// Callback functions
// *****

toggleSiteMenu = function() {
    if ($('#__int-toggle-site-menu').hasClass('inactive')) {
        // Show the menu
        $('#__int-toggle-site-menu').removeClass('inactive');
        $('#__int-toggle-site-menu').addClass('active');
        $('#__site-menu ul').slideDown('slow', function() {
            $('#__int-toggle-site-menu').html('Hide Menu');
        });
    } else {
        // Hide the menu
        $('#__site-menu ul').slideUp('slow', function() {
            $('#__int-toggle-site-menu').removeClass('active');
            $('#__int-toggle-site-menu').addClass('inactive');
            $('#__int-toggle-site-menu').html('Site Menu');
        });
    }
}
togglePageMenu = function() {
    if ($('#__int-toggle-page-menu').hasClass('inactive')) {
        // Show the menu
        $('#__int-toggle-page-menu').removeClass('inactive');
        $('#__int-toggle-page-menu').addClass('active');
        $('#__page-menu ul').slideDown('slow', function() {
            $('#__int-toggle-page-menu').html('Hide Menu');
        });
    } else {
        // Hide the menu
        $('#__page-menu ul').slideUp('slow', function() {
            $('#__int-toggle-page-menu').removeClass('active');
            $('#__int-toggle-page-menu').addClass('inactive');
            $('#__int-toggle-page-menu').html('Page Menu');
        });
    }
}
expandBox = function() {
    var content = $(this).parent().prev('pre').clone();
    $.fancybox({
        'content'   :   content,
        'padding'   :   20,
    });
}

// *****
// Code to setup formatting changes and callbacks
// *****

setupExpandableBoxes = function($boxes) {
    $linkBar = $('<div class="preLinkBar"></div>')
    .append($('<a class="expandBox"><img src="img/plus-icon.png"/>Expand</a>').click(expandBox))
    .append($('<a class="expandBox"><img src="img/copy-icon.png"/>Copy</a>').click(expandBox));
    
    $boxes
    .after($linkBar)
    .addClass('augmented');
}

setupExpandableImages = function($images) {
    $images.each(function() {
        var $imageLink = $('<a href="#" class="expandImage"></a>')
            .attr('href', $(this).attr('src'))
            .fancybox();
        $(this).wrap($imageLink);
    });
}

$(document).ready(function() {
    $('#__int-toggle-site-menu').click(toggleSiteMenu);
    $('#__int-toggle-page-menu').click(togglePageMenu);

    setupExpandableImages($('#__content img'));
    setupExpandableImages($('#__gallery img'));
    setupExpandableBoxes($('#__content pre'));
});