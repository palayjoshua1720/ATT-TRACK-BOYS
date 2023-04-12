// const button = document.getElementById("loginAuth");
//   button.addEventListener("click", () => {
//     console.log("working");
//   });

$(document).ready(function(){
  var Login = {
      Init: function(config) {
          this.config = config;
          this.BindEvents();
      },
      BindEvents: function() {
          let $this = this.config;            

            $this.btn_login.on('click', this.Login);
      },
      Login: ()  => {
        console.log("working");
        let $self = Login.config,
            $clean_data = {};

        $.each($self.form_login.serializeArray(), function(){
          $clean_data[this.name] = this.value;
        });

        $payload = {
          url : '/backoffice/authenticate',
          method_type: 'POST',
          payload: $clean_data
        }
      
        console.log($payload);

        const $common = new Common($payload)
        $common.ApiData()
        .then(async data => {
          if(data[0]['Result'] == 1){
            console.log("success");
            alert('success')
            window.location.href = '/backoffice/dashboard';
          }
          else{
            console.log("Failed");
          }
          // console.log(data)
          // alert(data[0]['Result'])

        })
        .catch(err => {
            console.log(err)
        })
        // let username = $this.input_user.val();
        // let password = $this.input_pass.val();       
        // console.log("Password: " + password);
      }
    }

    Login.Init({
      btn_login      : $('#loginAuth'),
      // input_user     : $('#authUser'),
      // input_pass     : $('#authPass'),
      form_login     : $('#form-login'),
    })
})