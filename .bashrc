#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'

# Prompt color
# PS1='[\u@\h \W]\$ '
export PS1="\[\e[36m\]\u\[\e[m\]\[\e[36m\]@\[\e[m\]\[\e[36m\]\h\[\e[m\]\[\e[36m\] \[\e[m\]\[\e[1;36m\]\w\[\e[m\]\[\e[36m\] \[\e[m\]\[\e[32m\] %\[\e[m\]\[\e[36m\] \[\e[m\]"

# Dir trim
export PROMPT_DIRTRIM=4
