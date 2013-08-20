function validate_file(field)
{
    with (field)
    {
        if (value==null||value==""){
            $('#myModal').modal();
            return false
        }
        else {return true}
    }
}


function validate_form(thisform)
{
    with (thisform)
    {
        if (validate_file(myfile)==false){
            myfile.focus();
            return false
        }
    }
}
