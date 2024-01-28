#!/bin/bash

cat /etc/bind/*.db | grep "NS"  | awk '{print $4}'
