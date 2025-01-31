import { Injectable, Logger } from '@nestjs/common';
import { Cron, CronExpression } from '@nestjs/schedule';
import { Octokit } from '@octokit/rest';
import { ConfigService } from '@nestjs/config';
import { CreateGithubJobDto } from './dto/create-github-job.dto';
import { UpdateGithubJobDto } from './dto/update-github-job.dto';

@Injectable()
export class GithubJobService {
  constructor(private configService: ConfigService) {}

  private readonly logger = new Logger(GithubJobService.name);
  private octokit = new Octokit({
    auth: this.configService.get('GITHUB_AUTH'),
  });

  // TODO: Schedule job to pull once, then job for checking for changes
  // TODO: Check if DB is empty for initial insert
  // @Cron(CronExpression.)
  async initialGithubRepoCronJob() {
    try {
      if (this.octokit) {
        const response = await this.octokit.request('GET /users/{username}/repos', {
          username: 'KwesiLarbi',
          headers: {
            "x-github-api-version": "2022-11-28",
          },
        });
        this.logger.log(response);
      }
      this.logger.log("AUTH didn't work");
    } catch (error) {
      this.logger.error(`Error grabbing repo data! ${JSON.stringify(error.response)}`);
    }
  }

  @Cron(CronExpression.EVERY_WEEKEND)
  async updateDatabse(id: number, updateGithubJobDto: UpdateGithubJobDto) {
    return `This action updates a #${id} githubJob`;
  }
  
  // remove(id: number) {
  //   return `This action removes a #${id} githubJob`;
  // }

  findAll() {
    return `This action returns all githubJob`;
  }

  findOne(id: number) {
    return `This action returns a #${id} githubJob`;
  }
}
