import { Module } from '@nestjs/common';
import { GithubJobService } from './github-job.service';
import { GithubJobController } from './github-job.controller';

@Module({
  controllers: [GithubJobController],
  providers: [GithubJobService],
})
export class GithubJobModule {}
