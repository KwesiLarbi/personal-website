import { PartialType } from '@nestjs/mapped-types';
import { CreateGithubJobDto } from './create-github-job.dto';

export class UpdateGithubJobDto extends PartialType(CreateGithubJobDto) {}
