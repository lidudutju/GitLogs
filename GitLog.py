# coding=utf-8
import sys, subprocess

__author__ = "lidu"


class Trigger(object):
    def getGitLogs(self):

        author_commits = subprocess.Popen(
            'git log --pretty=\'%cn\' | sort | uniq -c | sort -k1 -n -r ',
            shell=True, stdout=subprocess.PIPE)
        author_list = author_commits.stdout.readlines()
        for author in author_list:
            authorMap = author.split()
            command = 'git log --author=' + authorMap[
                1] + ' ' + '--pretty=tformat: --numstat | gawk \'{ add += $1 ; subs += $2} END {printf \"%s  %s \", add,subs }\' - '
            result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
            lines = result.stdout.readlines()
            spiltLine = lines[0].split()
            if spiltLine.__len__() >= 2:
                print "Author: ", authorMap[1], " Commits: " + authorMap[0], " Added Lines: ", spiltLine[
                    0], " Removed Lines: " + spiltLine[1]


t = Trigger()
t.getGitLogs()
