# explainerror
explain error in terminal by copilot, using .bashrc

~/.bashrcに以下を追加してください
alias c='xclip -selection clipboard && python3 ~/catkin_ws/src/copilot.py'
alias e='python3 ~/catkin_ws/src/explain.py'

上の通りのパスにファイルを配置するか、パスを適宜変えてください。
