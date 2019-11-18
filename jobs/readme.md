Job 列表
======
* 队列Job

        * * * * * { . ~/.bash_jobs && cd /home/share && python manager.py runjob -m queue/index ;} >> /home/share/logs/queue_list.`date +\%Y_\%m_\%d`.log 2>&1
        * * * * * { . ~/.bash_jobs && cd /home/share && python manager.py runjob -m pay/index ;} >> /home/share/logs/pay_index.`date +\%Y_\%m_\%d`.log 2>&1
        1 2 * * { . ~/.bash_jobs && cd /home/share && python manager.py runjob -m stat/daily -a member ;} >> /home/share/logs/pay_index.`date +\%Y_\%m_\%d`.log 2>&1
        2 2 * * * { . ~/.bash_jobs && cd /home/share && python manager.py runjob -m stat/daily -a food ;} >> /home/share/logs/pay_index.`date +\%Y_\%m_\%d`.log 2>&1
        3 2 * * * { . ~/.bash_jobs && cd /home/share && python manager.py runjob -m stat/daily -a site ;} >> /home/share/logs/pay_index.`date +\%Y_\%m_\%d`.log 2>&1