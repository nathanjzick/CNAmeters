# Powershell script to recursively convert image formats
# Configuration
$srcfolder = "C:\\Users\\plog1\\Documents\Scripts\\CNAmeters\\raw_bills\\"
$destfolder = "C:\\Users\\plog1\\Documents\\Scripts\\CNAmeters\\cleaned_images\\"
# This ps1 file will add copy files to designated folder
# Do NOT use Mogrify or the original images will be deleted
$im_convert_exe = "magick -density 300"
# change src_filter to the format of the source files
$src_filter = "*.pdf"
# change dest_ext to the format of the destination files
$dest_ext = "tiff"
$options = "-depth 8 -strip -background white -alpha off"
$logfile = "C:\\Users\\plog1\\Documents\Scripts\\CNAmeters\\convert.log"
$fp = New-Item -ItemType file $logfile -force
$count = 0
foreach ($srcitem in $(Get-ChildItem $srcfolder -include $src_filter -recurse))
{
    $srcname = $srcitem.fullname

    # Construct the filename and filepath for the output
    $partial = $srcitem.FullName.Substring( $srcitem.FullName.Length - 18, 18 )
    $destname = $destfolder + $partial
    $destname= [System.IO.Path]::ChangeExtension( $destname , $dest_ext )
    $destpath = [System.IO.Path]::GetDirectoryName( $destname )

    # Create the destination path if it does not exist
    if (-not (test-path $destpath))
    {
        New-Item $destpath -type directory | Out-Null
    }

    # Perform the conversion by calling an external tool
    $cmdline =  $im_convert_exe + " `"" + $srcname  + "`" " + $options + " `"" + $destname + "`" "
    # Write-Output $cmdline
    invoke-expression -command $cmdline

    # Get information about the output file
    $destitem = Get-item $destname

    # Show and record information comparing the input and output files
    $info = [string]::Format( "{0} `t {1} `t {2} `t {3} `t {4} `t {5}", $count,
	$partial, $srcname, $destname, $srcitem.Length ,  $destitem.Length)
    # Write-Output $info
    Add-Content $fp $info

    $count=$count+1
}