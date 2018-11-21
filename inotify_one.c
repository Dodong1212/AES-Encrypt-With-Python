#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/inotify.h>

#define EVENT_SIZE  ( sizeof (struct inotify_event) )
#define BUF_LEN     ( 1024 * ( EVENT_SIZE + 16 ) )

int main(int argc, char **argv) {
	char target[100]; // monitoring directory name
	int fd;
	int wd;
	char file_full_name[1024];
	char command[1024];
	char buffer[BUF_LEN];
	int length, i = 0;

	fd = inotify_init();
	if (fd < 0) {
		perror("inotify_init");
	}
	if (argc < 2) {
		fprintf(stderr, "Watching the current directory\n");
		strcpy(target, ".");
	}
	else {
		fprintf(stderr, "Watching '%s' directory\n", argv[1]);
		strcpy(target, argv[1]);
	}
	wd = inotify_add_watch(fd, target, IN_ALL_EVENTS);
	while (1) {
		length, i = 0;
		length = read(fd, buffer, BUF_LEN);
		if (length < 0) {
			perror("read");
		}
		while (i < length) {
			struct inotify_event *event = (struct inotify_event *) &buffer[i];
			if (event->len) {
				if (event->mask & IN_CREATE) {
					if (event->mask & IN_ISDIR) {
					}
					else {
						printf("%s IN_CREATE.\n", event->name);

						//DIR Encryption
						sprintf(command, "python AES_Encrypt_Python.py \"%s\"", target);

						system(command);
					}
				}
				else if (event->mask & IN_DELETE) {
					if (event->mask & IN_ISDIR) {
					}
					else {
						printf("%s  IN_DELETE.\n", event->name);
					}
				}
				else if (event->mask & IN_OPEN) {
					if (event->mask & IN_ISDIR) {
					}
					else {
						printf("%s IN_OPEN.\n", event->name);
					}
				}
				else if (event->mask & IN_MODIFY) {
					if (event->mask & IN_ISDIR) {
					}
					else {
						printf("%s IN_MODIFY.\n", event->name);
					}
				}
				else if (event->mask & IN_MOVED_FROM || event->mask & IN_MOVED_TO || event->mask & IN_MOVE_SELF) {
					if (event->mask & IN_ISDIR) {
					}
					else {

					}
				}
				else if (event->mask & IN_ACCESS) {
					if (event->mask & IN_ISDIR) {
					}
					else {
						printf("%s  IN_ACCESS.\n", event->name);
					}
				}
				else if (event->mask & IN_ATTRIB) {
					if (event->mask & IN_ISDIR) {
					}
					else {
						printf("%s  IN_ATTRIB.\n", event->name);
					}
				}
				else if (event->mask & IN_CLOSE_WRITE) {
					if (event->mask & IN_ISDIR) {
					}
					else {
						printf("%s  IN_CLOSE_WRITE.\n", event->name);
					}
				}
				else if (event->mask & IN_CLOSE_NOWRITE) {
					if (event->mask & IN_ISDIR) {
					}
					else {
						printf("%s  IN_CLOSE_NOWRITE.\n", event->name);
					}
				}
			}

			i += EVENT_SIZE + event->len;
		}
	}

	return 0;
}
