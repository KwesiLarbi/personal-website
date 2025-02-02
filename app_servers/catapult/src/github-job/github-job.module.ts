import { Module } from '@nestjs/common';
import { GithubJobService } from './github-job.service';
import { GithubJobController } from './github-job.controller';
import { TypeOrmModule } from '@nestjs/typeorm';
import { GithubRepo } from './entities/github-job.entity';

@Module({
  imports: [TypeOrmModule.forFeature([GithubRepo])],
  controllers: [GithubJobController],
  providers: [GithubJobService],
})
export class GithubJobModule {}
