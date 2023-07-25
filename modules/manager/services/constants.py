
password_options_ = ['year,month,min,hour,day',
                     'year,month,min,day,hour',
                     'year,month,hour,min,day',
                     'year,month,hour,day,min',
                     'year,month,day,min,hour',
                     'year,month,day,hour,min',
                     'year,min,month,hour,day',
                     'year,min,month,day,hour',
                     'year,min,hour,month,day',
                     'year,min,hour,day,month',
                     'year,min,day,month,hour',
                     'year,min,day,hour,month',
                     'year,hour,month,min,day',
                     'year,hour,month,day,min',
                     'year,hour,min,month,day',
                     'year,hour,min,day,month',
                     'year,hour,day,month,min',
                     'year,hour,day,min,month',
                     'year,day,month,min,hour',
                     'year,day,month,hour,min',
                     'year,day,min,month,hour',
                     'year,day,min,hour,month',
                     'year,day,hour,month,min',
                     'year,day,hour,min,month',
                     'month,year,min,hour,day',
                     'month,year,min,day,hour',
                     'month,year,hour,min,day',
                     'month,year,hour,day,min',
                     'month,year,day,min,hour',
                     'month,year,day,hour,min',
                     'month,min,year,hour,day',
                     'month,min,year,day,hour',
                     'month,min,hour,year,day',
                     'month,min,hour,day,year',
                     'month,min,day,year,hour',
                     'month,min,day,hour,year',
                     'month,hour,year,min,day',
                     'month,hour,year,day,min',
                     'month,hour,min,year,day',
                     'month,hour,min,day,year',
                     'month,hour,day,year,min',
                     'month,hour,day,min,year',
                     'month,day,year,min,hour',
                     'month,day,year,hour,min',
                     'month,day,min,year,hour',
                     'month,day,min,hour,year',
                     'month,day,hour,year,min',
                     'month,day,hour,min,year',
                     'min,year,month,hour,day',
                     'min,year,month,day,hour',
                     'min,year,hour,month,day',
                     'min,year,hour,day,month',
                     'min,year,day,month,hour',
                     'min,year,day,hour,month',
                     'min,month,year,hour,day',
                     'min,month,year,day,hour',
                     'min,month,hour,year,day',
                     'min,month,hour,day,year',
                     'min,month,day,year,hour',
                     'min,month,day,hour,year',
                     'min,hour,year,month,day',
                     'min,hour,year,day,month',
                     'min,hour,month,year,day',
                     'min,hour,month,day,year',
                     'min,hour,day,year,month',
                     'min,hour,day,month,year',
                     'min,day,year,month,hour',
                     'min,day,year,hour,month',
                     'min,day,month,year,hour',
                     'min,day,month,hour,year',
                     'min,day,hour,year,month',
                     'min,day,hour,month,year',
                     'hour,year,month,min,day',
                     'hour,year,month,day,min',
                     'hour,year,min,month,day',
                     'hour,year,min,day,month',
                     'hour,year,day,month,min',
                     'hour,year,day,min,month',
                     'hour,month,year,min,day',
                     'hour,month,year,day,min',
                     'hour,month,min,year,day',
                     'hour,month,min,day,year',
                     'hour,month,day,year,min',
                     'hour,month,day,min,year',
                     'hour,min,year,month,day',
                     'hour,min,year,day,month',
                     'hour,min,month,year,day',
                     'hour,min,month,day,year',
                     'hour,min,day,year,month',
                     'hour,min,day,month,year',
                     'hour,day,year,month,min',
                     'hour,day,year,min,month',
                     'hour,day,month,year,min',
                     'hour,day,month,min,year',
                     'hour,day,min,year,month',
                     'hour,day,min,month,year',
                     'day,year,month,min,hour',
                     'day,year,month,hour,min',
                     'day,year,min,month,hour',
                     'day,year,min,hour,month',
                     'day,year,hour,month,min',
                     'day,year,hour,min,month',
                     'day,month,year,min,hour',
                     'day,month,year,hour,min',
                     'day,month,min,year,hour',
                     'day,month,min,hour,year',
                     'day,month,hour,year,min',
                     'day,month,hour,min,year',
                     'day,min,year,month,hour',
                     'day,min,year,hour,month',
                     'day,min,month,year,hour',
                     'day,min,month,hour,year',
                     'day,min,hour,year,month',
                     'day,min,hour,month,year',
                     'day,hour,year,month,min',
                     'day,hour,year,min,month',
                     'day,hour,month,year,min',
                     'day,hour,month,min,year',
                     'day,hour,min,year,month',
                     'day,hour,min,month,year']

reset_pin_common_template = """
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Verify your login</title>
</head>

<body style="font-family: Helvetica, Arial, sans-serif; margin: 0px; padding: 0px; background-color: #ffffff;">
  <table role="presentation"
    style="width: 100%; border-collapse: collapse; border: 0px; border-spacing: 0px; font-family: Arial, Helvetica, sans-serif; background-color: rgb(239, 239, 239);">
    <tbody>
      <tr>
        <td align="center" style="padding: 1rem 2rem; vertical-align: top; width: 100%;">
          <table role="presentation" style="max-width: 600px; border-collapse: collapse; border: 0px; border-spacing: 0px; text-align: left;">
            <tbody>
              <tr>
                <td style="padding: 40px 0px 0px;">
                  <div style="padding: 20px; background-color: rgb(255, 255, 255);">
                    <div style="color: rgb(0, 0, 0); text-align: left;">
                      <h1 style="margin: 1rem 0">Security Pin</h1>
                      <p style="padding-bottom: 16px">Hello {}, Please remember your security pin includes your date of birth and current time in your mobile phone</p>
                      <p>Your security pin sequence is <strong style="font-size: 80%">{}</strong>.</p>
                      <p style="padding-bottom: 16px"> For example, Your Date Of Birth is may 8 2002 and current time in your mobile is afternoon 1:30 i.e (13:30) then your pin could be any of these <strong style="font-size: 90%">{}</strong></p>
                      <p style="padding-bottom: 16px"><i> Please remember this is only for security purpose only <br> If you don't want to use you can use custom pin </i></p>
                    </div>
                  </div>
                  <div style="padding-top: 20px; color: rgb(153, 153, 153); text-align: center;">
                    <p style="padding-bottom: 16px">Made in India</p>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </td>
      </tr>
    </tbody>
  </table>
</body>

</html>
"""

reset_pin_custom_template = """
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Verify your login</title>
</head>

<body style="font-family: Helvetica, Arial, sans-serif; margin: 0px; padding: 0px; background-color: #ffffff;">
  <table role="presentation"
    style="width: 100%; border-collapse: collapse; border: 0px; border-spacing: 0px; font-family: Arial, Helvetica, sans-serif; background-color: rgb(239, 239, 239);">
    <tbody>
      <tr>
        <td align="center" style="padding: 1rem 2rem; vertical-align: top; width: 100%;">
          <table role="presentation" style="max-width: 600px; border-collapse: collapse; border: 0px; border-spacing: 0px; text-align: left;">
            <tbody>
              <tr>
                <td style="padding: 40px 0px 0px;">
                  <div style="padding: 20px; background-color: rgb(255, 255, 255);">
                    <div style="color: rgb(0, 0, 0); text-align: left;">
                      <h1 style="margin: 1rem 0">Security Pin</h1>
                      <p style="padding-bottom: 16px">Hello {}, Please remember your security pin is <strong style="font-size: 80%">{}</strong>.</p>
                      <p style="padding-bottom: 16px"><i> Please remember this is custom pin <br> If you want you can use common pin for better security reasons </i></p>
                    </div>
                  </div>
                  <div style="padding-top: 20px; color: rgb(153, 153, 153); text-align: center;">
                    <p style="padding-bottom: 16px">Made in India</p>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </td>
      </tr>
    </tbody>
  </table>
</body>

</html>
"""

otp_message_template = """
<div style="font-family: Helvetica,Arial,sans-serif;min-width:1000px;overflow:auto;line-height:2">
  <div style="margin:50px auto;width:70%;padding:20px 0">
    <div style="border-bottom:1px solid #eee">
      <a href="" style="font-size:1.4em;color: #00466a;text-decoration:none;font-weight:600">Password Manager</a>
    </div>
    <p style="font-size:1.1em">Hi,</p>
    <p>Thank you for choosing Password Manager. Use the following OTP to complete your procedures. OTP is valid for 5 minutes</p>
    <h2 style="background: #00466a;margin: 0 auto;width: max-content;padding: 0 10px;color: #fff;border-radius: 4px;">{}</h2>
    <p style="font-size:0.9em;">Regards,<br />Password Manager</p>
    <hr style="border:none;border-top:1px solid #eee" />
    <div style="float:right;padding:8px 0;color:#aaa;font-size:0.8em;line-height:1;font-weight:300">
      <p>Password Manager Inc</p>
      <p>1600 Amphitheatre Parkway</p>
      <p>California</p>
    </div>
  </div>
</div>
"""