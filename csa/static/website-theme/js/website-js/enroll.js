function validate_login_form(){
    let email_regex = new RegExp(/^[\w\-\.\+]+\@[a-zA-Z0-9\.\-]+\.[a-zA-z0-9]{2,4}$/);
    let has_error = false;
    let mobile_el =  $("#mobile");
    let email_el =  $("#email");
    let full_name =  $("#full_name");
    if(!email_el.val()){
        // no value
        has_error = true;
        email_el.animateCss("shake");
    }
    else if(!email_regex.test(email_el.val())){
        // regex fail
        has_error = true;
        email_el.animateCss("shake");
    }
    else if(!full_name.val()){
        has_error = true;
        full_name.val("").animateCss("shake");
    }
    else if(!mobile_el.val()){
        has_error = true;
        mobile_el.val("").animateCss("shake");
    }
    return has_error
}

function enroll() {
    // loading on enroll button

    const body = {
        "fullname": $("#full_name").val(),
        "email": $("#email").val(),
        "mobile": $("#mobile").val(),
        "csrfmiddlewaretoken": "{{ csrf_token }}"
    };
    let settings = {
        url: '/enroll/',
        data: body,
        "success": function (response) {
            if(!response.status) {
                $("#email-error").attr("hidden", "hidden");
                $("#enroll-error").text(response.message);
            }
            else{
                window.location = "/enroll/"
            }
            $("#enroll_submit").attr("disabled", "disabled");
            show_notification("success", "Enroll Successful!");
        },
        "error": function () {
            show_notification("danger", "Something goes wrong. Please contact to admin");
        }};
        if(!validate_login_form()) {
            $("#enroll_submit").removeAttr("disabled");
            $.post(settings)
        }
        else{
            if ($("#full_name").val() && $("#email").val() && $("#mobile")){
                $("#email-error").removeAttr("hidden");
            }
            else{
                $("#email-error").attr("hidden", "hidden");
            }
        }
}