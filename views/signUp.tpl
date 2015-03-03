% rebase('master.tpl', title='Login')

<div class="container-fluid">
  <div class="row">
    <div class="col-xs-3 col-xs-offset-4">

      % setdefault('fullName', '')
      % setdefault('email', '')
      % setdefault('password', '')
      % setdefault('passwordCheck', '')
      <div class="panel panel-pop">
        <h3 class="panel-heading">Sign up</h3>
        <div class="panel-body">
          <form id="signup" action="signup" method="POST">
            <div class="form-group">
              <label for="fullName" class="sr-only">Full Name</label>
              <input id="fullName" name="fullName" placeholder="Full Name" value="{{fullName}}" class="form-control" />
            </div>
            <div class="form-group">
              <label for="email" class="sr-only">E-mail</label>
              <input id="email" name="email" placeholder="E-mail" value="{{email}}" class="form-control" />
            </div>
            <div class="form-group">
              <label for="password" class="sr-only">Password</label>
              <input name="password" placeholder="Password" value="{{password}}" class="form-control" />
            </div>
            <div class="form-group">
              <label for="passwordCheck" class="sr-only">Verify Password</label>
              <input name="passwordCheck" placeholder="Verify Password" value="{{passwordCheck}}" class="form-control" />
            </div>
            <button type="submit" class="btn btn-default">Sign up</button>
          </form>
        </div>
        <h5 class="panel-footer">Already signed up? <a href="/">Log in</a></h5>
      </div>

    </div>
  </div>
</div>

<script>
  $.backstretch("/images/splash2.jpg");
</script>
<script src="/scripts/signup.js"></script>