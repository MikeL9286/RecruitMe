<!DOCTYPE html>

<html>
  <head>
    <title>Welcome</title>
    <style type="text/css">
      .label {text-align: right}
      .error {color: red}
    </style>
  </head>

  <body>
    <form action="login" method="POST">
      <div>
        <label>Username: </label>
        <input name="username" placeholder="username" value="{{username}}" />
      </div>
      <div>
        <label>Password: </label>
        <input name="password" placeholder="password" value="{{password}}" />
      </div>    
      <button type="submit">Login</button>
      <label class="error">{{message}}</label>
    </form>
    <ul>
      <li><a href="/">Goto Home</a></li>
    </ul>
  </body>

</html>
