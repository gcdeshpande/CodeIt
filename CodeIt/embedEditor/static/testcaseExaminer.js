function testcaseExaminer(data) {
  var data= JSON.parse(data);
  $('#inputs').html(data.inputs.ips1);
  if(data.error=="") {
    $('#img1').attr("src",data.flagResult1);
    $('#img2').attr("src",data.flagResult2);
    $('#img3').attr("src",data.flagResult3);
    $('#img4').attr("src",data.flagResult4);

    $('#actualOutput1').html(data.actualOutput1);
    $('#userOutput1').html(data.userOutput1);
    $('#actualOutput2').html(data.actualOutput2);
    $('#userOutput2').html(data.userOutput2);
    $('#actualOutput3').html(data.actualOutput3);
    $('#userOutput3').html(data.userOutput3);
    $('#actualOutput4').html(data.actualOutput4);
    $('#userOutput4').html(data.userOutput4);
    $('#exampleModal').modal('show');

    if (data.done==1) {
      setTimeout(showNotify,5000);
      
    }
  }else{
    showError();
   }

   function showNotify() {
      timeoutid=setTimeout(function () {
       window.location.href="../index.php";
     }, 10000);
     $.notify({
    // options
    icon: 'glyphicon glyphicon-success-sign',
    title: '<strong>The program has been Compiled successfully and all test cases were satisfied.<br> You have Earned '+data.points+'XP  </strong><br>',
    message: 'Your Total Score is '+data.totalPoints+'XP<br>You will be redirected to mainpage in 10 sec ',
    target: '_blank'
  },{
    // settings
    element: 'body',
    position: null,
    type: "success",
    allow_dismiss: true,
    newest_on_top: true,
    showProgressbar: false,
    placement: {
      from: "top",
      align: "right"
    },
    offset: 20,
    spacing: 10,
    z_index: 1031,
    delay: 10000,
    timer: 1000,
    url_target: '_blank',
    mouse_over: null,
    animate: {
      enter: 'animated fadeInDown',
      exit: 'animated fadeOutUp'
    },
    onShow: null,
    onShown: null,
    onClose: null,
    onClosed: null,
    icon_type: 'class',
    template: '<div data-notify="container" class="col-xs-11 col-sm-3 alert alert-{0}" role="alert">' +
      '<button type="button" aria-hidden="true" class="close" data-notify="dismiss">×</button>' +
      '<span data-notify="icon"></span> ' +
      '<span data-notify="title">{1}</span> ' +
      '<span data-notify="message">{2}<br><br><a class="btn-link" href="../index.php">Redirect Now</a>&nbsp;<button class="btn-link" onclick="clearTimeout(timeoutid)">Stay Here</button></span>' +
    '</div>'
   });
   }
   function showError() {
     $.notify({
    // options
    icon: 'glyphicon glyphicon-success-sign',
    title: 'Error!<br>',
    message: '',
    target: '_blank'
  },{
    // settings
    element: 'body',
    position: null,
    type: "danger",
    allow_dismiss: true,
    newest_on_top: true,
    showProgressbar: false,
    placement: {
      from: "top",
      align: "right"
    },
    offset: 20,
    spacing: 10,
    z_index: 1031,
    delay: 10000,
    timer: 1000,
    url_target: '_blank',
    mouse_over: null,
    animate: {
      enter: 'animated fadeInDown',
      exit: 'animated fadeOutUp'
    },
    onShow: null,
    onShown: null,
    onClose: null,
    onClosed: null,
    icon_type: 'class',
    template: '<div data-notify="container" class="col-lg-6  alert alert-{0}" role="alert" style="">' +
      '<button type="button" aria-hidden="true" class="close" data-notify="dismiss">×</button>' +
      '<span data-notify="icon"></span> ' +
      '<span data-notify="title">{1}</span> ' +
      '<span data-notify="message">{2}<br><br><div>'+data.error+'<br></div> </span>' +
    '</div>'
   });
   }
}
