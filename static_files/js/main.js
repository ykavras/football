$(document).ready(function () {
    const ticketBtn = $('.ticket-btn');
    const form = $('form');
    const cropper = $('#cropper');
    const imageUpload = $('#upload-image');
    const imageBase64 = $('#imagebase64');
    const imgCrop = $('#img-crop');
    const closeForm = $('.close-form');
    let $uploadCrop;

    function readFile(input) {
        if (input.files && input.files[0]) {
            const reader = new FileReader();
            reader.onload = function (e) {
                $uploadCrop.croppie('bind', {
                    url: e.target.result
                });
                $('.ready').addClass('active');
            };
            reader.readAsDataURL(input.files[0]);
        }
    }

    $uploadCrop = imgCrop.croppie({
        viewport: {width: 200, height: 120},
        enableOrientation: true,
        mouseWheelZoom: 'ctrl'
    });

    imageUpload.on('change', function () {
        readFile(this);
    });

    cropper.on('click', function () {
        $uploadCrop.croppie('result', {
            type: 'canvas',
            size: 'original'
        }).then(function (resp) {
            imageBase64.val(resp);
        });
    });

    form.on('submit', function (e) {
        e.preventDefault();
        e.stopPropagation();
    });

    ticketBtn.on('click', function () {
        form.addClass('active');
    });

    closeForm.on('click', function () {
        form.removeClass('active');
    });
});