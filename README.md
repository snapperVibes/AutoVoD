# AutoVoD ✂
###### Quick script to help automate Pittsburgh Smash VoDs.
## Usage
Create an Excel worksheet with the match participants and timestamps.

`data.xlsx`

<table>
  <tbody>
    <tr>
      <td>Sam</td>
      <td>Perks</td>
      <td>0:24:32</td>
    </tr>
    <tr>
      <td>KAO</td>
      <td>Immortal</td>
      <td>0:48:21</td>
    </tr>
    <tr>
      <td>Dandy</td>
      <td>Lunar</td>
      <td>1:03:13</td>
    </tr>
  </tbody>
</table>

Open up the terminal. Assuming the worksheet, data, and VoD are in the current working directory,
run `python autovod.py --data data.xlsx --vod capture_footage.mp4`.

## Notes
This is a demo script. If it's actually used, quality of life changes can be easily added.
For example, `autovod` will currently break if two people fight twice.
