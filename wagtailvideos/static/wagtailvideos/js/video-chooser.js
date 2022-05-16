function createVideoChooser(id) {
    var chooserElement = $('#' + id + '-chooser');
    var previewVideo = chooserElement.find('.preview-image img');
    var input = $('#' + id);
    var editLink = chooserElement.find('.edit-link');

    document.addEventListener('DOMContentLoaded', event => {
        var input = $('#' + id);
        let call_url = window.chooserUrls.videoChooser + input.val();
        $.ajax(call_url).done(function(data) {
            let videoData = data.result
            input.val(videoData.id);
                    previewVideo.attr({
                        src: videoData.preview.url,
                        alt: videoData.title
                    });
                    chooserElement.removeClass('blank');
                    editLink.attr('href', videoData.edit_link);
        });
    });

    $('.action-clear', chooserElement).click(function() {
        input.val('');
        chooserElement.addClass('blank');
    });
}
